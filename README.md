# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_01:39:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,468 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 01:39:25 | Putupaula (Kalu Ganga) | 1.61 | 🟢 Normal | -0.002 |  |
| 2026-06-07 01:26:38 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-06-07 01:14:04 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.008 |  |
| 2026-06-07 01:10:28 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.010 |  |
| 2026-06-07 01:08:42 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-06-07 01:08:24 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:07:58 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-06-07 01:07:57 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.047 |  |
| 2026-06-07 01:06:50 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:06:16 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-06-07 01:06:01 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-06-07 01:05:48 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:05:45 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:05:17 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-06-07 01:05:01 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 01:04:40 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.019 |  |
| 2026-06-07 01:04:29 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:04:16 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:04:07 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | -0.033 |  |
| 2026-06-07 01:03:58 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:03:53 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 01:03:07 | Ellagawa (Kalu Ganga) | 7.09 | 🟢 Normal | -0.052 |  |
| 2026-06-07 01:02:59 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 01:02:37 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:02:00 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-07 01:01:42 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-07 01:01:27 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:00:10 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.074 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 01:03:53 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 00:05:04 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 01:05:01 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 01:02:00 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-07 01:02:59 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 01:05:45 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:05:48 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:01:27 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:07:58 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:36:37 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:03:58 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:41 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:04:29 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:02:37 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:08:24 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:06:50 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:10:31 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:05:19 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-07 01:39:25 | Putupaula (Kalu Ganga) | 1.61 | 🟢 Normal | -0.002 |  |
| 2026-06-07 01:14:04 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.008 |  |
| 2026-06-07 01:06:01 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-06-07 00:05:28 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-06-07 01:10:28 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.010 |  |
| 2026-06-07 01:05:17 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-06-07 01:07:58 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-06-07 01:01:42 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-07 01:04:40 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.019 |  |
| 2026-06-07 01:08:42 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-06-07 01:26:38 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-06-07 00:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | -0.023 |  |
| 2026-06-07 01:06:16 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-06-07 01:04:07 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | -0.033 |  |
| 2026-06-07 01:07:57 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.047 |  |
| 2026-06-07 00:03:01 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.050 |  |
| 2026-06-07 01:03:07 | Ellagawa (Kalu Ganga) | 7.09 | 🟢 Normal | -0.052 |  |
| 2026-06-07 01:00:10 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)