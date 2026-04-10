# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_21:19:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,601 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 21:19:30 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:12:20 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-04-10 21:12:14 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:08:13 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:07:41 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.029 |  |
| 2026-04-10 21:07:38 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-10 21:06:29 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:05:38 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 21:05:15 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:04:57 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:04:45 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-10 21:04:42 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:04:04 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:04:02 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:03:41 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-04-10 21:03:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-10 21:03:35 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:03:26 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-04-10 21:03:19 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:03:19 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.059 |  |
| 2026-04-10 21:03:02 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-10 21:02:36 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:02:34 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-04-10 21:02:33 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-04-10 21:02:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.041 |  |
| 2026-04-10 21:02:16 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-10 21:02:15 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:01:38 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.105 |  |
| 2026-04-10 21:01:31 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:01:15 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-10 21:01:08 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:00:53 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:00:27 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-10 21:00:26 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 18:06:03 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.886 | 🔺 Rising |
| 2026-04-10 21:03:41 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-04-10 21:03:26 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-04-10 21:12:20 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-04-10 21:07:38 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-10 21:04:45 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-10 21:03:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-10 21:00:27 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-10 21:02:16 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-10 21:03:02 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-10 21:05:38 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 21:01:08 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:00:26 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:00:53 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:02:36 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:06:29 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:04:04 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:03:35 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:04:02 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:05:15 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:19:30 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:04:42 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:08:13 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:01:31 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:03:19 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:02:15 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:04:57 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-10 20:01:15 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:01:15 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-10 21:02:34 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-04-10 21:02:33 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-04-10 21:07:41 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.029 |  |
| 2026-04-10 21:02:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.041 |  |
| 2026-04-10 21:03:19 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.059 |  |
| 2026-04-10 21:01:38 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)