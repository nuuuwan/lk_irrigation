# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_03:38:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,625 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 03:38:20 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -1.440 |  |
| 2026-05-10 03:37:55 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -1.440 |  |
| 2026-05-10 03:37:30 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -1.440 |  |
| 2026-05-10 03:33:48 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -144.000 |  |
| 2026-05-10 03:33:23 | Panadugama (Nilwala Ganga) | 3.48 | 🟢 Normal | -144.000 |  |
| 2026-05-10 03:16:57 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -3.273 |  |
| 2026-05-10 03:16:35 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -3.273 |  |
| 2026-05-10 03:16:09 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.057 |  |
| 2026-05-10 03:13:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | -2.571 |  |
| 2026-05-10 03:12:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -2.571 |  |
| 2026-05-10 03:12:52 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.105 |  |
| 2026-05-10 03:09:39 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-10 03:07:07 | Katharagama (Menik Ganga) | 1.59 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-10 03:06:48 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.028 |  |
| 2026-05-10 03:06:27 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.009 |  |
| 2026-05-10 03:06:18 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:06:18 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.029 |  |
| 2026-05-10 03:04:51 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:04:47 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-10 03:04:44 | Thanamalwila (Kirindi Oya) | 3.61 | 🟢 Normal | 1.393 | 🔺 Rising |
| 2026-05-10 03:04:41 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.931 | 🔺 Rising |
| 2026-05-10 03:04:21 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.042 |  |
| 2026-05-10 03:03:52 | Thaldena (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.184 |  |
| 2026-05-10 03:03:46 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 03:03:45 | Moragaswewa (Deduru Oya) | 3.48 | 🟢 Normal | -0.141 |  |
| 2026-05-10 03:03:42 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:03:23 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:03:20 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:03:04 | Nakkala (Kumbukkan Oya) | 2.06 | 🟢 Normal | -0.337 |  |
| 2026-05-10 03:02:51 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:02:43 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -6.750 |  |
| 2026-05-10 03:02:27 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -6.750 |  |
| 2026-05-10 03:01:59 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.039 |  |
| 2026-05-10 03:01:57 | Kuda Oya (Kirindi Oya) | 2.63 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-05-10 03:01:50 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:01:41 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-05-10 03:01:38 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-10 03:01:16 | Wellawaya (Kirindi Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:00:11 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2026-05-10 02:58:32 | Wellawaya (Kirindi Oya) | 2.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 03:04:44 | Thanamalwila (Kirindi Oya) | 3.61 | 🟢 Normal | 1.393 | 🔺 Rising |
| 2026-05-10 03:04:41 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.931 | 🔺 Rising |
| 2026-05-10 03:01:57 | Kuda Oya (Kirindi Oya) | 2.63 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-05-09 18:02:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-10 03:01:38 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-10 03:07:07 | Katharagama (Menik Ganga) | 1.59 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-10 03:09:39 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-10 03:03:46 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 03:03:42 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:01:16 | Wellawaya (Kirindi Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:02:51 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:03:23 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:01:50 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:01:34 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:00:11 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:04:51 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:03:20 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:06:18 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:06:27 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.009 |  |
| 2026-05-10 02:02:31 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-10 03:04:47 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-10 03:01:41 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-05-10 03:06:48 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.028 |  |
| 2026-05-10 03:06:18 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.029 |  |
| 2026-05-10 03:01:59 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.039 |  |
| 2026-05-10 03:04:21 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.042 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-10 03:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2026-05-10 03:16:09 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.057 |  |
| 2026-05-09 18:04:22 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.081 |  |
| 2026-05-10 03:12:52 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.105 |  |
| 2026-05-10 03:03:45 | Moragaswewa (Deduru Oya) | 3.48 | 🟢 Normal | -0.141 |  |
| 2026-05-10 03:03:52 | Thaldena (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.184 |  |
| 2026-05-10 03:03:04 | Nakkala (Kumbukkan Oya) | 2.06 | 🟢 Normal | -0.337 |  |
| 2026-05-10 03:38:20 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -1.440 |  |
| 2026-05-10 03:13:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | -2.571 |  |
| 2026-05-10 03:16:57 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -3.273 |  |
| 2026-05-10 03:02:43 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -6.750 |  |
| 2026-05-10 03:33:48 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)