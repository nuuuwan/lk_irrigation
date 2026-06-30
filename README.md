# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_04:40:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,023 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 04:40:40 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:35:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.040 |  |
| 2026-07-01 04:28:59 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:10:53 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.017 |  |
| 2026-07-01 04:09:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.57 | 🟢 Normal | -0.030 |  |
| 2026-07-01 04:08:30 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.019 |  |
| 2026-07-01 04:07:52 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.020 |  |
| 2026-07-01 04:07:43 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.018 |  |
| 2026-07-01 04:05:52 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:05:13 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.130 |  |
| 2026-07-01 04:04:54 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.033 |  |
| 2026-07-01 04:04:36 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:04:28 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-01 04:04:25 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-07-01 04:04:23 | Ellagawa (Kalu Ganga) | 6.57 | 🟢 Normal | -0.152 |  |
| 2026-07-01 04:04:17 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-07-01 04:04:16 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.013 |  |
| 2026-07-01 04:04:15 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:04:11 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.068 |  |
| 2026-07-01 04:03:55 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:03:39 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:03:14 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.252 |  |
| 2026-07-01 04:03:09 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:02:57 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:02:50 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:02:42 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:02:11 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:01:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:01:16 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 04:01:12 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.070 |  |
| 2026-07-01 04:00:46 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 04:04:28 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-01 03:36:38 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-01 04:01:16 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 04:03:55 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:01:15 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:40:40 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:02:57 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:01:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:04:36 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:04:15 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:08:51 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:03:09 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:05:30 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:11:16 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:02:11 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:02:50 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:00:46 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:28:59 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:05:52 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:02:00 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:08:16 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:02:42 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-01 04:04:17 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-06-30 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-01 04:04:25 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-07-01 04:04:16 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.013 |  |
| 2026-07-01 04:10:53 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.017 |  |
| 2026-07-01 04:07:43 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.018 |  |
| 2026-07-01 04:08:30 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.019 |  |
| 2026-07-01 04:07:52 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.020 |  |
| 2026-07-01 04:09:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.57 | 🟢 Normal | -0.030 |  |
| 2026-07-01 04:04:54 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.033 |  |
| 2026-07-01 04:35:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.040 |  |
| 2026-07-01 04:04:11 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.068 |  |
| 2026-07-01 04:01:12 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.070 |  |
| 2026-07-01 04:05:13 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.130 |  |
| 2026-07-01 04:04:23 | Ellagawa (Kalu Ganga) | 6.57 | 🟢 Normal | -0.152 |  |
| 2026-07-01 04:03:14 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.252 |  |
| 2026-07-01 03:07:14 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -273.103 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)