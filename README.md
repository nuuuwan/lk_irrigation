# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_21:41:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,482 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 21:41:05 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:30:18 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:10:08 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:09:45 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-04-11 21:07:50 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-11 21:07:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-04-11 21:05:23 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-04-11 21:05:19 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-11 21:05:13 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:05:12 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-11 21:03:52 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:03:20 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:02:56 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-11 21:02:48 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-11 21:02:47 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-04-11 21:02:43 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:02:42 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.045 |  |
| 2026-04-11 21:02:42 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-11 21:02:29 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:02:28 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:02:26 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:02:23 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.010 |  |
| 2026-04-11 21:02:18 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 21:02:14 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:02:11 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-04-11 21:02:08 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:01:55 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.139 |  |
| 2026-04-11 21:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:01:46 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:01:36 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.087 |  |
| 2026-04-11 21:01:15 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.450 | 🔺 Rising |
| 2026-04-11 21:01:10 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:01:08 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:01:00 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-11 21:00:37 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-11 21:00:09 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 21:01:15 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.450 | 🔺 Rising |
| 2026-04-11 21:02:42 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-11 21:01:00 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-11 21:05:19 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-11 21:02:48 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-11 21:00:37 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-11 21:07:50 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-11 21:05:12 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-11 21:02:18 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 21:01:46 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:01:08 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:41:05 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:02:29 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:05:13 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:00:09 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 18:03:33 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:02:43 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:03:52 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 20:02:16 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:02:28 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:30:18 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:02:26 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:03:20 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:10:08 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:01:10 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:02:14 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-11 21:02:56 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-11 18:00:38 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-11 21:02:23 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.010 |  |
| 2026-04-11 21:07:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-04-11 21:05:23 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-04-11 21:09:45 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-04-11 21:02:47 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-04-11 21:02:11 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-04-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.040 |  |
| 2026-04-11 21:02:42 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.045 |  |
| 2026-04-11 21:01:36 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.087 |  |
| 2026-04-11 21:01:55 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)