# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_18:05:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,696 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 18:05:46 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:05:18 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-06-20 18:04:15 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-20 18:04:13 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:04:06 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:03:37 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:03:03 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 48.000 | 🔺 Rising |
| 2026-06-20 18:03:02 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:03:00 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 48.000 | 🔺 Rising |
| 2026-06-20 18:02:56 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:02:49 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:02:41 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.089 |  |
| 2026-06-20 18:02:41 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.011 |  |
| 2026-06-20 18:02:34 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.041 |  |
| 2026-06-20 18:02:30 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-20 18:02:28 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:02:19 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | -0.020 |  |
| 2026-06-20 18:02:18 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | -0.041 |  |
| 2026-06-20 18:02:15 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-20 18:02:09 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.011 |  |
| 2026-06-20 18:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:01:44 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:33 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:32 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:28 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:28 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:19 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:13 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:04 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-06-20 18:00:47 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-20 18:00:22 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.011 |  |
| 2026-06-20 17:19:15 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:17:59 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.038 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 18:03:03 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 48.000 | 🔺 Rising |
| 2026-06-20 18:04:15 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-20 18:02:15 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-20 18:00:47 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-20 18:02:30 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-20 17:17:59 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-20 17:07:26 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-20 17:03:06 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-20 18:01:28 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:03:02 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:33 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:32 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:04:13 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:02:12 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:02:56 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:04:06 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:02:28 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:28 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:05:46 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:15 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:44 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:19 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:02:34 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:13 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:14 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 18:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:02:49 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:03:37 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:00:22 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.011 |  |
| 2026-06-20 18:02:09 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.011 |  |
| 2026-06-20 18:05:18 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-06-20 18:02:41 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.011 |  |
| 2026-06-20 18:01:04 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-06-20 16:01:55 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-06-20 18:02:19 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | -0.020 |  |
| 2026-06-20 18:02:18 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | -0.041 |  |
| 2026-06-20 18:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.041 |  |
| 2026-06-20 18:02:41 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)