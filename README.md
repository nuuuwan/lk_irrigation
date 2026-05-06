# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_16:30:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,547 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 16:30:27 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-06 16:29:55 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-06 16:19:18 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:16:00 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:14:13 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:12:15 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:08:43 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:08:42 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:08:18 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:07:57 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:07:52 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-05-06 16:06:23 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-06 16:06:23 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-05-06 16:05:27 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-06 16:05:20 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:04:59 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.010 |  |
| 2026-05-06 16:04:58 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-05-06 16:04:58 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-06 16:04:41 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:04:16 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:04:16 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-05-06 16:03:48 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:03:17 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:02:43 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-06 16:02:40 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:02:23 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.020 |  |
| 2026-05-06 16:02:22 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:02:21 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-05-06 16:02:11 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:01:52 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:01:44 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:01:41 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-06 16:01:18 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-05-06 16:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:01:15 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:01:09 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-06 16:00:51 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:00:48 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:00:35 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 16:04:58 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-06 16:30:27 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-06 16:02:43 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-06 16:05:27 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-06 16:06:23 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-06 15:03:10 | Baddegama (Gin Ganga) | 0.77 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 16:29:55 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-06 16:03:48 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:01:44 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:01:52 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:00:48 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:08:18 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:07:57 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:14:13 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:19:18 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:12:15 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:04:16 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:04:41 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:01:15 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:00:35 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:03:17 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:02:11 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:05:20 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:02:22 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:16:00 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:08:43 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:02:40 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:00:51 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-06 16:04:59 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.010 |  |
| 2026-05-06 16:01:41 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-06 16:06:23 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-05-06 16:01:09 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-06 16:04:58 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-05-06 16:02:23 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.020 |  |
| 2026-05-06 16:04:16 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-05-06 16:07:52 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-05-06 16:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-05-06 16:01:18 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.030 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)