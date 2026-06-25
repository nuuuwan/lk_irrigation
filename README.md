# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_22:20:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,349 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 22:20:27 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:18:35 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-06-25 22:13:37 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:11:47 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.182 |  |
| 2026-06-25 22:10:01 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:10:00 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:08:48 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:07:55 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:07:39 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-25 22:07:10 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:06:55 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.012 |  |
| 2026-06-25 22:06:29 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 21:03:44 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-06-25 22:04:11 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.342 | 🔺 Rising |
| 2026-06-25 22:00:15 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-06-25 22:02:18 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-25 22:04:12 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-25 22:07:39 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-25 22:00:32 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 22:02:32 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 22:02:06 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 22:03:37 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:05:17 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:10:01 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:07:55 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:10:00 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:03:22 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:07:10 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:08:48 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:03:53 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:13:37 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:03:38 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:02:39 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 18:02:21 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:06:29 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:20:27 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:04:44 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-25 22:18:35 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-06-25 22:03:53 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-06-25 22:05:14 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-06-25 22:05:42 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:02:25 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-25 22:06:55 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.012 |  |
| 2026-06-25 22:02:49 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-06-25 22:01:17 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.021 |  |
| 2026-06-25 22:02:12 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.023 |  |
| 2026-06-25 20:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.024 |  |
| 2026-06-25 22:04:09 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.031 |  |
| 2026-06-25 22:11:47 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)