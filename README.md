# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_18:13:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,671 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 18:13:18 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-02 18:11:26 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:10:12 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-02-02 18:09:57 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:08:33 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:08:21 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.044 |  |
| 2026-02-02 18:07:44 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:07:17 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:06:22 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:05:23 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:04:53 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-02 18:04:39 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-02 18:04:25 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-02-02 18:04:20 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-02 18:04:14 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-02-02 18:03:45 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-02-02 18:03:35 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-02-02 18:03:33 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:03:26 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-02 18:03:24 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:03:20 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:03:07 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:03:03 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:02:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.179 |  |
| 2026-02-02 18:02:46 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:02:37 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-02 18:02:22 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 18:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:02:14 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:02:11 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:01:59 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-02 18:01:43 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | -0.068 |  |
| 2026-02-02 18:01:23 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:01:17 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.061 |  |
| 2026-02-02 18:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.041 |  |
| 2026-02-02 18:00:54 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:00:45 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:00:34 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-02-02 18:00:22 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-02-02 18:00:11 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-02-02 18:00:09 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 18:04:25 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-02-02 18:04:14 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-02-02 18:10:12 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-02-02 18:13:18 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-02 18:04:39 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-02 18:01:59 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-02 18:04:53 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-02 18:02:22 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 18:03:24 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:00:09 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:07:44 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:03:33 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:08:33 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:09:57 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:11:26 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:06:22 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:02:46 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:07:17 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:03:07 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:00:54 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:05:23 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:03:20 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:02:14 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:02:37 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-02 18:04:20 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-02 18:00:22 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-02-02 18:00:34 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-02-02 18:03:35 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-02-02 18:00:11 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-02-02 18:01:23 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:00:45 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-02 18:03:45 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-02-02 18:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.041 |  |
| 2026-02-02 18:08:21 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.044 |  |
| 2026-02-02 18:01:17 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.061 |  |
| 2026-02-02 18:01:43 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | -0.068 |  |
| 2026-02-02 18:02:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.179 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)