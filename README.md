# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_12:25:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,698 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 12:25:07 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.008 |  |
| 2026-02-15 12:12:51 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:09:17 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-02-15 12:07:41 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:07:12 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:05:56 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:05:47 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:05:41 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:05:24 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.029 |  |
| 2026-02-15 12:05:22 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.010 |  |
| 2026-02-15 12:05:20 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:04:37 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-02-15 12:04:27 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:04:26 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-15 12:04:13 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:03:46 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:03:34 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.040 |  |
| 2026-02-15 12:03:32 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 12:03:30 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:03:23 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-15 12:03:16 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:03:15 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:03:09 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 12:02:51 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 12:02:47 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:02:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-15 12:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | -0.070 |  |
| 2026-02-15 12:02:34 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:02:19 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:02:16 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-15 12:02:10 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:02:09 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-15 12:02:01 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.078 |  |
| 2026-02-15 12:01:59 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-02-15 12:01:30 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 12:01:26 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:00:48 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:00:31 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-02-15 12:00:25 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-15 12:00:13 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | -0.241 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 12:01:59 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-02-15 12:02:09 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-15 12:02:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-15 12:03:23 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-15 12:04:26 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-15 12:01:30 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 12:02:51 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 12:03:09 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 12:03:32 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 12:05:56 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:01:26 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:03:15 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:07:12 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:05:47 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:05:20 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:02:10 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:00:48 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:03:16 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:04:27 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:05:41 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:07:41 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:03:30 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:03:46 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:12:51 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:02:47 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:02:34 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 12:25:07 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.008 |  |
| 2026-02-15 12:02:16 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-15 12:05:22 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.010 |  |
| 2026-02-15 12:00:25 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-15 12:00:31 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-02-15 12:09:17 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-02-15 12:05:24 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.029 |  |
| 2026-02-15 12:04:37 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-02-15 12:03:34 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.040 |  |
| 2026-02-15 12:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | -0.070 |  |
| 2026-02-15 12:02:01 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.078 |  |
| 2026-02-15 12:00:13 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | -0.241 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)