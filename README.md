# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_08:07:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **181,631 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 08:07:44 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:07:00 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-06-17 08:05:37 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:05:05 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:04:50 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-06-17 08:04:00 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-06-17 08:03:59 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.049 |  |
| 2026-06-17 08:03:58 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-06-17 08:03:55 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-06-17 08:03:24 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-06-17 08:03:15 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-06-17 08:03:10 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.086 |  |
| 2026-06-17 08:02:59 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:48 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 08:02:46 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.030 |  |
| 2026-06-17 08:02:44 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.064 |  |
| 2026-06-17 08:02:42 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:42 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:33 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:27 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.059 |  |
| 2026-06-17 08:02:25 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | -0.020 |  |
| 2026-06-17 08:02:15 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.032 |  |
| 2026-06-17 08:02:11 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:11 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 08:02:10 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:03 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:01 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.020 |  |
| 2026-06-17 08:01:38 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:01:37 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-06-17 08:01:30 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-17 08:01:17 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.130 |  |
| 2026-06-17 08:00:23 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 07:22:53 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 08:02:11 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 08:02:48 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 08:02:11 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:00:23 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 07:01:50 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:10 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:05:05 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-17 05:02:49 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:05:37 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:25 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:03:55 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:33 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:42 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-17 07:05:17 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:03 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:01:38 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 07:09:40 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:07:44 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-17 08:02:59 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 07:11:56 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.009 |  |
| 2026-06-17 08:07:00 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-06-17 08:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-06-17 08:01:30 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-17 08:03:58 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-06-17 08:04:00 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-06-17 08:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | -0.020 |  |
| 2026-06-17 08:04:50 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-06-17 08:02:01 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.020 |  |
| 2026-06-17 08:03:24 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-06-17 08:01:37 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-06-17 07:10:20 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.026 |  |
| 2026-06-17 08:03:15 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-06-17 08:02:46 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.030 |  |
| 2026-06-17 08:02:15 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.032 |  |
| 2026-06-17 08:03:59 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.049 |  |
| 2026-06-17 08:02:27 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.059 |  |
| 2026-06-17 08:02:44 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.064 |  |
| 2026-06-17 08:03:10 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.086 |  |
| 2026-06-17 08:01:17 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)