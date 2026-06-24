# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_21:11:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,408 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 21:11:56 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:10:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.61 | 🟢 Normal | -0.027 |  |
| 2026-06-24 21:10:38 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:08:17 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:08:13 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-24 21:07:40 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:07:30 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.011 |  |
| 2026-06-24 21:07:07 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.075 |  |
| 2026-06-24 21:06:10 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.113 |  |
| 2026-06-24 21:05:31 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-24 21:05:05 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | -0.028 |  |
| 2026-06-24 21:05:03 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:04:53 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:04:16 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:04:08 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.012 |  |
| 2026-06-24 21:03:45 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:03:41 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.011 |  |
| 2026-06-24 21:03:35 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-06-24 21:03:16 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-06-24 21:03:07 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:03:01 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-24 21:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:02:48 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:02:47 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-06-24 21:02:47 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:02:25 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:02:12 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.050 |  |
| 2026-06-24 21:02:11 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-24 21:01:59 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.021 |  |
| 2026-06-24 21:01:59 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.041 |  |
| 2026-06-24 21:01:47 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:01:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:01:31 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-24 21:01:21 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:00:58 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:00:37 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 21:02:47 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-06-24 21:08:13 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-24 21:03:01 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-24 20:03:12 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-24 21:01:21 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:02:48 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:11:56 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:01:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:07:40 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:21 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:10:38 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:04:53 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:03:07 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:03:45 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:00:58 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:04:16 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:01:47 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:08:17 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:00:37 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 21:02:25 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:16:07 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.009 |  |
| 2026-06-24 21:02:11 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-24 21:05:31 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-24 21:01:31 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-24 21:03:41 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.011 |  |
| 2026-06-24 21:07:30 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.011 |  |
| 2026-06-24 21:04:08 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.012 |  |
| 2026-06-24 21:01:59 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.021 |  |
| 2026-06-24 21:10:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.61 | 🟢 Normal | -0.027 |  |
| 2026-06-24 21:05:05 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | -0.028 |  |
| 2026-06-24 21:03:16 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-06-24 21:03:35 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-06-24 21:01:59 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.041 |  |
| 2026-06-24 21:02:12 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.050 |  |
| 2026-06-24 21:07:07 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.075 |  |
| 2026-06-24 21:06:10 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)