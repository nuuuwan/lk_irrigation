# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_10:14:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,790 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 10:14:56 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.045 |  |
| 2026-05-11 10:14:13 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:12:22 | Galgamuwa (Mee Oya) | 1.80 | 🟢 Normal | -0.080 |  |
| 2026-05-11 10:10:15 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 6.171 | 🔺 Rising |
| 2026-05-11 10:09:40 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 6.171 | 🔺 Rising |
| 2026-05-11 10:09:34 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-11 10:08:51 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 10:08:41 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-11 10:08:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-05-11 10:08:07 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-05-11 10:08:05 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.149 |  |
| 2026-05-11 10:07:01 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-11 10:06:53 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 10:06:31 | Moraketiya (Walawe Ganga) | 1.47 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-11 10:06:20 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-11 10:05:43 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:05:32 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-05-11 10:05:25 | Thanamalwila (Kirindi Oya) | 2.74 | 🟢 Normal | -0.163 |  |
| 2026-05-11 10:05:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:04:59 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 10:04:49 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:04:34 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-11 10:03:46 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:03:27 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.050 |  |
| 2026-05-11 10:02:35 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:02:34 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-05-11 10:02:33 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:02:23 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 10:02:16 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.032 |  |
| 2026-05-11 10:02:09 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-11 10:02:04 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-05-11 10:01:48 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.030 |  |
| 2026-05-11 10:01:27 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.080 |  |
| 2026-05-11 10:01:13 | Katharagama (Menik Ganga) | 2.02 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-05-11 10:01:08 | Kuda Oya (Kirindi Oya) | 2.94 | 🟢 Normal | -0.101 |  |
| 2026-05-11 10:00:59 | Thanthirimale (Malwathu Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:00:34 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 10:10:15 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 6.171 | 🔺 Rising |
| 2026-05-11 10:08:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-05-11 10:01:13 | Katharagama (Menik Ganga) | 2.02 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-05-11 09:14:33 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-11 10:06:20 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-11 10:02:09 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-11 10:07:01 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-11 10:06:31 | Moraketiya (Walawe Ganga) | 1.47 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-11 10:08:41 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-11 10:06:53 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 10:02:23 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 10:09:34 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-11 10:08:51 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 10:04:59 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 10:03:46 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:14:13 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:02:35 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:02:33 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:05:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:05:43 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:04:49 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:00:59 | Thanthirimale (Malwathu Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-05-11 10:04:34 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-11 10:02:04 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-05-11 10:08:07 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-05-11 09:07:30 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-05-11 10:05:32 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-05-11 10:02:34 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-05-11 09:03:32 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-05-11 10:01:48 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.030 |  |
| 2026-05-11 10:02:16 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.032 |  |
| 2026-05-11 10:00:34 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.040 |  |
| 2026-05-11 10:14:56 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.045 |  |
| 2026-05-11 10:03:27 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.050 |  |
| 2026-05-11 10:01:27 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.080 |  |
| 2026-05-11 10:12:22 | Galgamuwa (Mee Oya) | 1.80 | 🟢 Normal | -0.080 |  |
| 2026-05-11 10:01:08 | Kuda Oya (Kirindi Oya) | 2.94 | 🟢 Normal | -0.101 |  |
| 2026-05-11 10:08:05 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.149 |  |
| 2026-05-11 10:05:25 | Thanamalwila (Kirindi Oya) | 2.74 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)