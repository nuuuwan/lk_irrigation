# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_21:25:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,300 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 21:25:20 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-22 21:19:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-04-22 21:16:16 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-04-22 21:15:52 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-04-22 21:11:02 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-22 21:08:25 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-22 21:07:45 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-04-22 21:06:25 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-04-22 21:06:12 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.096 |  |
| 2026-04-22 21:06:10 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-22 21:05:55 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-22 21:05:49 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-22 21:05:22 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-22 21:05:12 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-04-22 21:05:01 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.105 |  |
| 2026-04-22 21:04:58 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 21:04:36 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-22 21:04:17 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:04:12 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.049 |  |
| 2026-04-22 21:03:46 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:03:03 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:02:45 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.049 |  |
| 2026-04-22 21:02:43 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:02:34 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:02:24 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 21:02:22 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-22 21:02:20 | Thanamalwila (Kirindi Oya) | 3.40 | 🟢 Normal | 1.610 | 🔺 Rising |
| 2026-04-22 21:02:11 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:02:08 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:01:33 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:01:20 | Kuda Oya (Kirindi Oya) | 3.72 | 🟢 Normal | -0.429 |  |
| 2026-04-22 21:01:19 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:01:05 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-22 21:00:54 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:00:35 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | -0.179 |  |
| 2026-04-22 21:00:27 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-04-22 21:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.250 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 21:02:20 | Thanamalwila (Kirindi Oya) | 3.40 | 🟢 Normal | 1.610 | 🔺 Rising |
| 2026-04-22 21:00:27 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-04-22 21:16:16 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-04-22 21:05:12 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-04-22 21:08:25 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-22 21:06:10 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-22 21:04:36 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-22 21:25:20 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-22 21:01:05 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-22 21:05:49 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 21:05:22 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-22 21:05:55 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-22 21:11:02 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-22 21:02:24 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 21:04:58 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 21:02:43 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:01:33 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:03:46 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:01:19 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:04:17 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:02:11 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:03:03 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:00:54 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:02:08 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:19:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-04-22 21:07:45 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-22 21:02:22 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:52 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 21:15:52 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-04-22 21:06:25 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-04-22 21:04:12 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.049 |  |
| 2026-04-22 21:02:45 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.049 |  |
| 2026-04-22 21:06:12 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.096 |  |
| 2026-04-22 21:05:01 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.105 |  |
| 2026-04-22 21:00:35 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | -0.179 |  |
| 2026-04-22 21:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.250 |  |
| 2026-04-22 21:01:20 | Kuda Oya (Kirindi Oya) | 3.72 | 🟢 Normal | -0.429 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)