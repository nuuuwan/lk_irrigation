# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_15:14:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **204,326 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 15:14:42 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.045 |  |
| 2026-07-12 15:09:07 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:08:32 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.038 |  |
| 2026-07-12 15:07:55 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:07:48 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:07:18 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:06:05 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:06:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-07-12 15:05:57 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:05:49 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.005 |  |
| 2026-07-12 15:05:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:04:32 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:04:02 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-07-12 15:04:01 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-12 15:03:42 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-07-12 15:03:29 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-07-12 15:03:25 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 15:03:00 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:02:51 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-12 15:02:49 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:02:35 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:02:31 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.019 |  |
| 2026-07-12 15:02:16 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:02:15 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-07-12 15:02:15 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:02:12 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.010 |  |
| 2026-07-12 15:02:10 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:01:58 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:01:56 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-12 15:01:50 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.062 |  |
| 2026-07-12 15:01:49 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:01:31 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 15:01:28 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:00:59 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-07-12 15:00:58 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:00:42 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-12 15:00:09 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 15:03:29 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-07-12 15:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-12 15:01:56 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-12 15:02:51 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-12 15:00:42 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-12 15:03:25 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 15:01:31 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 15:05:49 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.005 |  |
| 2026-07-12 15:01:49 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:02:10 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:07:48 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:01:58 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:02:16 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:00:09 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:05:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:09:07 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-12 14:13:12 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:01:28 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:02:49 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:04:32 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:02:15 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:06:05 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:07:55 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:04:01 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:07:18 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:02:35 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:00:58 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:03:00 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:02:12 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.010 |  |
| 2026-07-12 15:03:42 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-07-12 15:02:15 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-07-12 15:02:31 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.019 |  |
| 2026-07-12 15:04:02 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-07-12 15:00:59 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-07-12 15:08:32 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.038 |  |
| 2026-07-12 15:14:42 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.045 |  |
| 2026-07-12 15:06:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-07-12 15:01:50 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)