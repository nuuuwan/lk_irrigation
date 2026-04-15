# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_09:19:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,590 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 09:19:11 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:15:23 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.060 |  |
| 2026-04-15 09:12:35 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:11:33 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-15 09:08:55 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:08:44 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.028 |  |
| 2026-04-15 09:07:41 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.235 |  |
| 2026-04-15 09:07:35 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:07:30 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:07:10 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.018 |  |
| 2026-04-15 09:06:39 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.010 |  |
| 2026-04-15 09:05:35 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:05:28 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-15 09:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.049 |  |
| 2026-04-15 09:04:47 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 09:04:38 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:04:29 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-04-15 09:04:08 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-04-15 09:04:05 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-04-15 09:04:02 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-04-15 09:03:58 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-04-15 09:03:58 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:03:30 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-04-15 09:03:30 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 09:03:28 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:03:20 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-04-15 09:03:16 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:03:00 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:02:58 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.051 |  |
| 2026-04-15 09:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-15 09:02:11 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:02:10 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:02:03 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.013 |  |
| 2026-04-15 09:01:56 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-15 09:01:55 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-04-15 09:01:42 | Thanthirimale (Malwathu Oya) | 2.74 | 🟢 Normal | -0.039 |  |
| 2026-04-15 09:01:37 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:01:34 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-15 09:01:24 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:01:09 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-04-15 09:00:37 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 09:04:08 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-04-15 09:11:33 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-15 09:05:28 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-15 09:03:30 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 09:01:34 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-15 09:04:47 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 09:02:10 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:02:11 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:19:11 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:05:35 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:01:37 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:03:16 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:03:00 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:07:30 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:12:35 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:03:28 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:04:38 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:07:35 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:01:24 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:08:55 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:01:56 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-15 09:03:30 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-04-15 09:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-15 09:06:39 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.010 |  |
| 2026-04-15 09:01:55 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-04-15 08:04:24 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-04-15 09:02:03 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.013 |  |
| 2026-04-15 09:07:10 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.018 |  |
| 2026-04-15 09:04:29 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-04-15 09:01:09 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-04-15 08:00:49 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-04-15 09:08:44 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.028 |  |
| 2026-04-15 09:03:20 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-04-15 09:01:42 | Thanthirimale (Malwathu Oya) | 2.74 | 🟢 Normal | -0.039 |  |
| 2026-04-15 09:00:37 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.040 |  |
| 2026-04-15 09:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.049 |  |
| 2026-04-15 09:02:58 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.051 |  |
| 2026-04-15 09:15:23 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.060 |  |
| 2026-04-15 09:07:41 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.235 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)