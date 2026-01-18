# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_21:14:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **49,290 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 21:14:53 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:14:01 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:11:29 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:10:50 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:10:21 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.026 |  |
| 2026-01-18 21:10:16 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:08:37 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:07:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:05:29 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.038 |  |
| 2026-01-18 21:05:12 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-18 21:05:09 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.341 | 🔺 Rising |
| 2026-01-18 21:04:40 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:04:29 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:04:09 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-01-18 21:03:55 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:03:48 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:03:43 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:03:27 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:03:25 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.097 |  |
| 2026-01-18 21:03:25 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:03:10 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:03:04 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:02:51 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:02:47 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-01-18 21:02:46 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:02:35 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-18 21:02:35 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:02:28 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:02:23 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:01:51 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:01:43 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-01-18 21:00:55 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:00:33 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-18 20:29:06 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 21:05:09 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.341 | 🔺 Rising |
| 2026-01-18 21:05:12 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-18 21:01:51 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:02:46 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:00:55 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:02:28 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:02:23 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:01:43 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-18 18:05:15 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:10:50 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:10:16 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:03:55 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:03:04 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:11:29 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-18 20:00:34 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:08:37 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:02:51 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:02:35 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-18 20:01:29 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:00:33 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:03:27 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:03:10 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:04:40 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:04:29 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:14:53 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-18 18:01:56 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:14:01 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:03:43 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:03:48 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:07:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-18 21:04:09 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-01-18 21:02:35 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-18 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.020 |  |
| 2026-01-18 21:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-01-18 21:10:21 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.026 |  |
| 2026-01-18 21:02:47 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-01-18 21:05:29 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.038 |  |
| 2026-01-18 20:01:55 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.082 |  |
| 2026-01-18 21:03:25 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)