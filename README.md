# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_22:14:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,233 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 22:14:38 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-23 22:12:46 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-23 22:10:43 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:10:06 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-23 22:08:42 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.037 |  |
| 2026-04-23 22:08:20 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-23 22:08:11 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-04-23 22:06:23 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.122 |  |
| 2026-04-23 22:06:14 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-23 22:04:31 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:04:29 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:04:24 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-04-23 22:04:15 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.022 |  |
| 2026-04-23 22:04:09 | Thanamalwila (Kirindi Oya) | 2.50 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-23 22:04:06 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:03:49 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-04-23 22:03:46 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:03:32 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:03:18 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:03:03 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:02:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-04-23 22:02:27 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-04-23 22:02:15 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-23 22:02:13 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-23 22:02:07 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-23 22:02:04 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-23 22:01:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:01:09 | Kuda Oya (Kirindi Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:01:00 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:00:58 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 22:00:55 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-23 21:26:28 | Thanamalwila (Kirindi Oya) | 2.46 | 🟢 Normal | 0.064 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 22:02:27 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-04-23 21:01:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-04-23 22:04:24 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-04-23 22:02:15 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-23 22:08:20 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-23 22:06:14 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-23 22:04:09 | Thanamalwila (Kirindi Oya) | 2.50 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-23 22:12:46 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-23 22:02:13 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-23 22:10:06 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-23 22:00:55 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-23 22:14:38 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-23 22:00:58 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 21:04:11 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-23 18:03:04 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 21:05:59 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-23 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:04:06 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:01:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:01:00 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:03:18 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:04:29 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:03:46 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:03:32 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:10:43 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:04:31 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:01:09 | Kuda Oya (Kirindi Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-04-23 22:08:11 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-04-23 22:02:04 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:03:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-23 22:02:07 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-23 21:01:19 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-04-23 21:00:18 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-04-23 22:04:15 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.022 |  |
| 2026-04-23 22:03:49 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-04-23 22:02:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-04-23 22:08:42 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.037 |  |
| 2026-04-23 21:01:06 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | -0.069 |  |
| 2026-04-23 22:06:23 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)