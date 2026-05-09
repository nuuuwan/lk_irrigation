# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_18:01:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,267 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 18:01:37 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 18:00:47 | Kuda Oya (Kirindi Oya) | 2.24 | 🟢 Normal | -0.076 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-09 18:00:16 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-09 18:00:10 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-09 17:40:29 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 17:19:25 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.054 |  |
| 2026-05-09 17:18:28 | Katharagama (Menik Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-09 17:11:29 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-05-09 17:09:55 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-09 17:09:15 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.030 |  |
| 2026-05-09 17:08:57 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.015 |  |
| 2026-05-09 17:08:56 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.028 |  |
| 2026-05-09 17:07:59 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-09 17:07:55 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.050 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 17:07:55 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-09 17:03:43 | Moragaswewa (Deduru Oya) | 3.65 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-09 17:01:59 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 17:01:29 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 17:06:20 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 18:00:10 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-09 18:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 17:09:55 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-09 17:00:04 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:01:37 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 17:03:31 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-09 17:06:48 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-09 17:07:59 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-09 17:18:28 | Katharagama (Menik Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-09 17:00:20 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-09 17:11:29 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-05-09 17:03:34 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-09 17:01:32 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-09 17:04:17 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-05-09 18:00:16 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-09 17:02:30 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-09 17:01:26 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-09 17:08:57 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.015 |  |
| 2026-05-09 16:01:00 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-05-09 17:08:56 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.028 |  |
| 2026-05-09 17:09:15 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.030 |  |
| 2026-05-09 17:03:07 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-05-09 17:06:59 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.032 |  |
| 2026-05-09 17:01:13 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.040 |  |
| 2026-05-09 17:05:26 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | -0.048 |  |
| 2026-05-09 17:06:15 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.050 |  |
| 2026-05-09 17:02:48 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.050 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-09 17:01:47 | Thanamalwila (Kirindi Oya) | 2.27 | 🟢 Normal | -0.053 |  |
| 2026-05-09 17:19:25 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.054 |  |
| 2026-05-09 18:00:47 | Kuda Oya (Kirindi Oya) | 2.24 | 🟢 Normal | -0.076 |  |
| 2026-05-09 17:05:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.36 | 🟢 Normal | -0.095 |  |
| 2026-05-09 17:01:43 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.099 |  |
| 2026-05-09 17:03:38 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)