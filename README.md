# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_09:34:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,709 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 09:34:20 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:19:44 | Pitabeddara (Nilwala Ganga) | 2.01 | 🟢 Normal | 6.023 | 🔺 Rising |
| 2026-04-14 09:13:31 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-04-14 09:13:02 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | -0.025 |  |
| 2026-04-14 09:12:33 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.017 |  |
| 2026-04-14 09:10:38 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.066 |  |
| 2026-04-14 09:08:37 | Kithulgala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:07:57 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:07:55 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.083 |  |
| 2026-04-14 09:06:57 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:06:51 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:06:28 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.019 |  |
| 2026-04-14 09:05:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.076 |  |
| 2026-04-14 09:04:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:04:29 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.019 |  |
| 2026-04-14 09:04:11 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 09:04:09 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-04-14 09:03:58 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-14 09:03:58 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-04-14 09:03:40 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.089 |  |
| 2026-04-14 09:03:37 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-14 09:03:33 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-04-14 09:02:52 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-04-14 09:02:48 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-04-14 09:02:48 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-14 09:02:40 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:02:36 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.033 |  |
| 2026-04-14 09:02:21 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-04-14 09:02:12 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 6.023 | 🔺 Rising |
| 2026-04-14 09:01:59 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:01:58 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.040 |  |
| 2026-04-14 09:01:56 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.049 |  |
| 2026-04-14 09:01:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:01:28 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-04-14 09:01:27 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.123 |  |
| 2026-04-14 09:01:12 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:01:10 | Thanthirimale (Malwathu Oya) | 4.26 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-14 09:00:48 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-04-14 09:00:17 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-14 09:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 09:19:44 | Pitabeddara (Nilwala Ganga) | 2.01 | 🟢 Normal | 6.023 | 🔺 Rising |
| 2026-04-14 09:00:17 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-14 09:01:10 | Thanthirimale (Malwathu Oya) | 4.26 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-14 09:04:11 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 09:08:37 | Kithulgala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:34:20 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:01:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:06:51 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:01:12 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:07:57 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:04:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:01:59 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:02:40 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:06:57 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 09:13:31 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-04-14 09:03:58 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-14 09:03:58 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-04-14 09:02:21 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-04-14 09:02:48 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-14 09:03:37 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-14 09:12:33 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.017 |  |
| 2026-04-14 09:06:28 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.019 |  |
| 2026-04-14 09:04:29 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.019 |  |
| 2026-04-14 09:02:48 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-04-14 09:03:33 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-04-14 09:00:48 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-04-14 09:13:02 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | -0.025 |  |
| 2026-04-14 09:02:52 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-04-14 09:01:28 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-04-14 09:04:09 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-04-14 09:02:36 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.033 |  |
| 2026-04-14 09:01:58 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.040 |  |
| 2026-04-14 09:01:56 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.049 |  |
| 2026-04-14 09:10:38 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.066 |  |
| 2026-04-14 09:05:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.076 |  |
| 2026-04-14 09:07:55 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.083 |  |
| 2026-04-14 09:03:40 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.089 |  |
| 2026-04-14 09:01:27 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)