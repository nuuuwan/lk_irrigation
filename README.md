# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_14:19:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,821 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 14:19:19 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-06-27 14:14:54 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:12:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | -0.008 |  |
| 2026-06-27 14:11:59 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.019 |  |
| 2026-06-27 14:11:54 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-06-27 14:11:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:11:46 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-27 14:09:13 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-27 14:08:47 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-06-27 14:08:42 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 14:07:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-27 14:07:08 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:06:49 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:06:18 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:05:51 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:05:45 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-27 14:05:27 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.019 |  |
| 2026-06-27 14:04:57 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 14:04:48 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 14:04:45 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:04:22 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:03:57 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-27 14:03:57 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-06-27 14:03:52 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:03:47 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-06-27 14:03:20 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:03:08 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 14:02:49 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:02:46 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-27 14:02:37 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-06-27 14:02:28 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-27 14:02:17 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:02:10 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:02:02 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-06-27 14:01:56 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-27 14:01:25 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.010 |  |
| 2026-06-27 14:01:07 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:00:52 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:00:21 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 14:05:45 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-27 14:01:56 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-27 14:09:13 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-27 14:08:42 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 14:07:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-27 14:03:57 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-27 14:04:48 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 14:04:57 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 14:03:08 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 14:11:46 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-27 14:04:45 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:11:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:04:22 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:03:20 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:14:54 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:03:52 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:07:08 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:02:49 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:02:10 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:06:49 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:05:51 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:02:17 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:00:52 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:06:18 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:01:07 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 14:12:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | -0.008 |  |
| 2026-06-27 14:11:54 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-06-27 14:02:28 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-27 14:02:46 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-27 14:03:47 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-06-27 14:01:25 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.010 |  |
| 2026-06-27 14:00:21 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-27 14:02:02 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-06-27 14:11:59 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.019 |  |
| 2026-06-27 14:02:37 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-06-27 14:05:27 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.019 |  |
| 2026-06-27 14:19:19 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-06-27 14:03:57 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-06-27 14:08:47 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.029 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)