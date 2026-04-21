# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_21:27:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,400 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 21:27:05 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 21:16:51 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:11:08 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.045 |  |
| 2026-04-21 21:10:37 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.042 |  |
| 2026-04-21 21:08:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.055 |  |
| 2026-04-21 21:07:22 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.125 |  |
| 2026-04-21 21:07:07 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.041 |  |
| 2026-04-21 21:06:56 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:06:43 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-21 21:06:23 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-21 21:06:22 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.116 |  |
| 2026-04-21 21:06:13 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-21 21:05:57 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.010 |  |
| 2026-04-21 21:05:33 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 21:05:17 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.029 |  |
| 2026-04-21 21:05:00 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:04:52 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-04-21 21:04:49 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-21 21:04:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:04:40 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.048 |  |
| 2026-04-21 21:04:02 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:03:53 | Thanamalwila (Kirindi Oya) | 2.35 | 🟢 Normal | 0.710 | 🔺 Rising |
| 2026-04-21 21:03:48 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.049 |  |
| 2026-04-21 21:03:27 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-21 21:03:01 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-04-21 21:02:52 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:02:43 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:02:07 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.205 |  |
| 2026-04-21 21:01:55 | Kuda Oya (Kirindi Oya) | 3.60 | 🟢 Normal | 1.002 | 🔺 Rising |
| 2026-04-21 21:01:49 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.050 |  |
| 2026-04-21 21:01:38 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-21 21:01:34 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 21:01:34 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-21 21:01:33 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.040 |  |
| 2026-04-21 21:00:40 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.083 |  |
| 2026-04-21 21:00:14 | Wellawaya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.339 |  |
| 2026-04-21 20:56:02 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 21:01:55 | Kuda Oya (Kirindi Oya) | 3.60 | 🟢 Normal | 1.002 | 🔺 Rising |
| 2026-04-21 21:03:53 | Thanamalwila (Kirindi Oya) | 2.35 | 🟢 Normal | 0.710 | 🔺 Rising |
| 2026-04-21 21:04:52 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-04-21 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-21 21:01:38 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-21 21:06:23 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-21 21:06:43 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-21 21:01:34 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-21 21:06:13 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-21 18:03:15 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-21 21:27:05 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 21:03:27 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-21 21:05:33 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 21:01:34 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 21:04:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:02:52 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:04:02 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:01:33 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:02:43 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:16:51 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:06:56 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:04:49 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-21 21:05:57 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.010 |  |
| 2026-04-21 21:03:01 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-04-21 21:05:17 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.029 |  |
| 2026-04-21 21:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.040 |  |
| 2026-04-21 21:07:07 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.041 |  |
| 2026-04-21 21:10:37 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.042 |  |
| 2026-04-21 21:11:08 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.045 |  |
| 2026-04-21 21:04:40 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.048 |  |
| 2026-04-21 21:03:48 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.049 |  |
| 2026-04-21 21:01:49 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.050 |  |
| 2026-04-21 21:08:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.055 |  |
| 2026-04-21 21:00:40 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.083 |  |
| 2026-04-21 21:06:22 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.116 |  |
| 2026-04-21 21:07:22 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.125 |  |
| 2026-04-21 21:02:07 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.205 |  |
| 2026-04-21 21:00:14 | Wellawaya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.339 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)