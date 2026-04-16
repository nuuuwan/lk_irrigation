# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_17:21:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,802 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 17:21:16 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-16 17:12:10 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.037 |  |
| 2026-04-16 17:10:57 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:10:16 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:09:23 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 17:09:02 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 17:08:43 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:07:18 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.047 |  |
| 2026-04-16 17:06:46 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:05:59 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:05:38 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-04-16 17:04:46 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-16 17:04:41 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.127 |  |
| 2026-04-16 17:03:57 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:03:50 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-04-16 17:03:31 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:03:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.088 |  |
| 2026-04-16 17:03:27 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.012 |  |
| 2026-04-16 17:03:25 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-04-16 17:03:21 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | 14.400 | 🔺 Rising |
| 2026-04-16 17:03:02 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-04-16 17:03:01 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:02:47 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:02:40 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:02:35 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-04-16 17:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-04-16 17:02:25 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-04-16 17:02:22 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:02:21 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:02:10 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:02:06 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 14.400 | 🔺 Rising |
| 2026-04-16 17:01:24 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:01:22 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:01:09 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:00:55 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:00:39 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-04-16 17:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-16 17:00:06 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 17:03:21 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | 14.400 | 🔺 Rising |
| 2026-04-16 17:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-16 17:09:23 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 17:09:02 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 17:21:16 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-16 17:01:09 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:00:06 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:03:01 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:01:22 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:01:24 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:02:10 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:03:31 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:02:22 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:10:16 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:06:46 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:08:43 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:03:57 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:02:47 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:02:21 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:10:57 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:05:59 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:00:55 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-16 17:02:40 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 16:01:55 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-16 17:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-04-16 17:04:46 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-16 17:02:25 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-04-16 17:03:25 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-04-16 17:03:27 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.012 |  |
| 2026-04-16 17:03:02 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-04-16 17:03:50 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-04-16 17:02:35 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-04-16 17:05:38 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-04-16 17:12:10 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.037 |  |
| 2026-04-16 17:00:39 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-04-16 17:07:18 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.047 |  |
| 2026-04-16 16:00:15 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.080 |  |
| 2026-04-16 17:03:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.088 |  |
| 2026-04-16 17:04:41 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)