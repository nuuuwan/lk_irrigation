# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_23:31:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,825 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 23:31:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-27 23:19:29 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:09:30 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.106 |  |
| 2026-04-27 23:09:23 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:08:58 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:08:11 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:07:50 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-04-27 23:07:15 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:06:37 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:05:19 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-04-27 23:05:16 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-27 23:05:13 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.009 |  |
| 2026-04-27 23:04:59 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-27 23:04:39 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-04-27 23:04:23 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-27 23:03:46 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:03:22 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 23:03:15 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:03:00 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 23:02:57 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-04-27 23:02:55 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.040 |  |
| 2026-04-27 23:02:40 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-27 23:02:30 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-04-27 23:01:51 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.080 |  |
| 2026-04-27 23:01:33 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-27 23:01:18 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-27 23:00:41 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 23:00:16 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 23:02:57 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-04-27 23:02:30 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-04-27 22:01:32 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-27 23:05:16 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-27 23:04:59 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-27 23:31:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-27 23:04:23 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-27 23:03:00 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 23:03:22 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 23:02:40 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-27 18:05:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 22:02:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 23:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 23:08:11 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:07:15 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:02:17 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:00:44 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:03:19 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:08:58 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:03:15 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:03:46 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:09:23 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:06:37 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:19:29 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:00:41 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-27 23:07:50 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-04-27 23:05:13 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.009 |  |
| 2026-04-27 23:01:18 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-27 23:01:33 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-27 23:00:16 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-27 22:04:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | -0.013 |  |
| 2026-04-27 23:04:39 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-04-27 23:05:19 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-04-27 23:02:55 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.040 |  |
| 2026-04-27 22:07:59 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.072 |  |
| 2026-04-27 23:01:51 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.080 |  |
| 2026-04-27 23:09:30 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)