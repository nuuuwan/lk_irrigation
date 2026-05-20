# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_22:12:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,327 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 22:12:12 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-05-20 22:12:12 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-20 22:07:24 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:07:12 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.023 |  |
| 2026-05-20 22:06:59 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.029 |  |
| 2026-05-20 22:06:16 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-05-20 22:06:03 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:05:48 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-20 22:04:39 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.098 |  |
| 2026-05-20 22:04:25 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-20 22:04:00 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:03:23 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:03:10 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-20 22:02:58 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:50 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.041 |  |
| 2026-05-20 22:02:50 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.062 |  |
| 2026-05-20 22:02:46 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:42 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:41 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:27 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:15 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:03 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:00 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:01:55 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:01:50 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:01:31 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:01:28 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.026 |  |
| 2026-05-20 22:01:14 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 22:01:07 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-20 22:00:54 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 21:01:47 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-20 22:03:10 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-20 22:04:25 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-20 22:05:48 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-20 22:01:07 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-20 21:16:20 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-20 22:01:14 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 22:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-20 22:02:58 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:01:24 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:00:54 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:03:23 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:42 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:01:50 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:03:48 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:12:12 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:03 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:04:00 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:27 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:15 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:00 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:46 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:07:24 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:02:41 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:06:03 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:01:31 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:01:55 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-20 22:06:16 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-05-20 22:12:12 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-05-20 18:01:19 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-20 22:07:12 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.023 |  |
| 2026-05-20 22:01:28 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.026 |  |
| 2026-05-20 22:06:59 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.029 |  |
| 2026-05-20 18:02:19 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-05-20 21:07:49 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-05-20 22:02:50 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.041 |  |
| 2026-05-20 22:02:50 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.062 |  |
| 2026-05-20 22:04:39 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)