# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_16:12:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,874 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 16:12:18 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:09:15 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:09:12 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.018 |  |
| 2026-07-07 16:09:00 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:08:53 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:08:50 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.017 |  |
| 2026-07-07 16:08:07 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:07:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-07 16:07:35 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:07:19 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:07:10 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | -0.009 |  |
| 2026-07-07 16:05:03 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-07 16:04:52 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:04:52 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.071 |  |
| 2026-07-07 16:04:14 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.029 |  |
| 2026-07-07 16:03:56 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:03:46 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-07 16:03:32 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.049 |  |
| 2026-07-07 16:03:17 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.041 |  |
| 2026-07-07 16:03:14 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-07 16:03:08 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-07 16:03:08 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-07-07 16:02:40 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:02:25 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.263 |  |
| 2026-07-07 16:02:19 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-07-07 16:02:16 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:02:12 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-07 16:01:28 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-07-07 16:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:01:14 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:01:13 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:00:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:00:54 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:00:46 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:00:19 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:00:14 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:00:11 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 16:07:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-07 16:02:12 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-07 15:03:05 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-07 16:05:03 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-07 16:03:14 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-07 16:00:11 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:00:14 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:02:40 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:07:19 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:00:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:01:13 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:12:18 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:09:15 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:03:56 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 15:04:34 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:07:35 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:02:16 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:04:14 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:08:07 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:00:46 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:01:14 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:09:00 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:08:53 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:00:19 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:00:54 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-07 16:07:10 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | -0.009 |  |
| 2026-07-07 16:03:46 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-07 16:03:08 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-07 16:03:08 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-07-07 16:08:50 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.017 |  |
| 2026-07-07 16:09:12 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.018 |  |
| 2026-07-07 16:02:19 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-07-07 16:01:28 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-07-07 16:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.029 |  |
| 2026-07-07 16:03:17 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.041 |  |
| 2026-07-07 16:03:32 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.049 |  |
| 2026-07-07 16:04:52 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.071 |  |
| 2026-07-07 16:02:25 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.263 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)