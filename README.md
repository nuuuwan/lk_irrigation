# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_14:57:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,242 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 14:57:06 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-08 14:12:48 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.034 |  |
| 2026-05-08 14:10:37 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -30.000 |  |
| 2026-05-08 14:10:19 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -30.000 |  |
| 2026-05-08 14:09:10 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.018 |  |
| 2026-05-08 14:08:59 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | -0.039 |  |
| 2026-05-08 14:08:09 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.056 |  |
| 2026-05-08 14:07:34 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-08 14:07:05 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.150 |  |
| 2026-05-08 14:06:39 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 14:01:04 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal | 4.235 | 🔺 Rising |
| 2026-05-08 14:05:15 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-05-08 14:04:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-08 14:04:16 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-08 14:06:20 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-08 14:02:54 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-08 14:00:17 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-08 14:07:34 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-08 14:57:06 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-08 14:01:02 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-08 14:02:20 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-08 14:01:42 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-08 14:04:18 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-08 14:01:56 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-08 14:02:17 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-08 14:00:56 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-08 14:02:53 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-08 14:02:01 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-05-08 14:00:10 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-08 14:03:42 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-05-08 14:09:10 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.018 |  |
| 2026-05-08 13:00:11 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.021 |  |
| 2026-05-08 14:00:40 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.028 |  |
| 2026-05-08 14:01:57 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.030 |  |
| 2026-05-08 14:06:39 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.033 |  |
| 2026-05-08 14:12:48 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.034 |  |
| 2026-05-08 14:03:08 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.036 |  |
| 2026-05-08 14:08:59 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | -0.039 |  |
| 2026-05-08 14:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | -0.039 |  |
| 2026-05-08 13:01:53 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.039 |  |
| 2026-05-08 14:01:32 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.040 |  |
| 2026-05-08 14:08:09 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.056 |  |
| 2026-05-08 14:04:23 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.059 |  |
| 2026-05-08 14:04:51 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.083 |  |
| 2026-05-08 14:01:19 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.085 |  |
| 2026-05-08 14:04:42 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | -0.085 |  |
| 2026-05-08 14:04:04 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | -0.089 |  |
| 2026-05-08 14:07:05 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.150 |  |
| 2026-05-08 14:10:37 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -30.000 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)