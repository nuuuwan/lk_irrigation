# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_07:10:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,098 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 07:10:03 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.018 |  |
| 2026-06-03 07:09:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.171 |  |
| 2026-06-03 07:08:44 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.018 |  |
| 2026-06-03 07:08:32 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-03 07:07:51 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-03 07:07:33 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-06-03 07:06:57 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 07:05:58 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:05:56 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 07:05:53 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:05:29 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-06-03 07:05:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.022 |  |
| 2026-06-03 07:05:23 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-06-03 07:05:23 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 07:05:09 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:04:39 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:03:27 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.030 |  |
| 2026-06-03 07:03:27 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-06-03 07:03:26 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:03:22 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:03:15 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-03 07:02:54 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | -0.004 |  |
| 2026-06-03 07:02:54 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:02:42 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-03 07:02:40 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.188 |  |
| 2026-06-03 07:02:35 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-06-03 07:02:29 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.094 |  |
| 2026-06-03 07:02:27 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:02:24 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.011 |  |
| 2026-06-03 07:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:01:40 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:01:08 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:00:33 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.050 |  |
| 2026-06-03 07:00:14 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-03 06:55:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.171 |  |
| 2026-06-03 06:41:26 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.001 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 06:05:04 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-03 07:07:51 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-03 07:02:42 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-03 06:16:51 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-03 07:08:32 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-03 07:05:23 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 06:04:47 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 07:05:56 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 07:06:57 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 07:00:14 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:02:27 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:01:40 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:05:53 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:01:08 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:02:54 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:03:26 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:05:58 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:05:09 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:04:39 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 07:03:22 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-03 06:41:26 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.001 |  |
| 2026-06-03 07:02:54 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | -0.004 |  |
| 2026-06-03 07:07:33 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-06-03 07:03:15 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-03 07:02:24 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.011 |  |
| 2026-06-03 07:02:35 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-06-03 07:10:03 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.018 |  |
| 2026-06-03 07:08:44 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.018 |  |
| 2026-06-03 07:05:29 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-06-03 07:05:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.022 |  |
| 2026-06-03 07:03:27 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.030 |  |
| 2026-06-03 07:05:23 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-06-03 06:01:50 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.033 |  |
| 2026-06-03 07:03:27 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-06-03 07:00:33 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.050 |  |
| 2026-06-03 07:02:29 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.094 |  |
| 2026-06-03 07:09:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.171 |  |
| 2026-06-03 07:02:40 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.188 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)