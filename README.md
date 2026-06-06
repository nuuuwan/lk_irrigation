# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_00:36:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,440 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 00:36:37 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:35:48 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.627 | 🔺 Rising |
| 2026-06-07 00:14:49 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:11:13 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:10:31 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:09:27 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | -0.028 |  |
| 2026-06-07 00:08:47 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 00:07:58 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:06:52 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:06:42 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-07 00:06:18 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-06-07 00:05:28 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-06-07 00:05:19 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:05:08 | Ellagawa (Kalu Ganga) | 7.14 | 🟢 Normal | -0.009 |  |
| 2026-06-07 00:05:04 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 00:04:25 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-06-07 00:04:24 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-07 00:04:23 | Rathnapura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.063 |  |
| 2026-06-07 00:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | -0.023 |  |
| 2026-06-07 00:03:47 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:03:37 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:03:34 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:03:01 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.050 |  |
| 2026-06-07 00:03:00 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.023 |  |
| 2026-06-07 00:02:55 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-06-07 00:02:36 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 00:02:34 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-07 00:02:26 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:02:16 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:02:13 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:02:09 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:01:21 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.021 |  |
| 2026-06-07 00:01:20 | Thalgahagoda (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.627 | 🔺 Rising |
| 2026-06-07 00:01:18 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-06-07 00:01:11 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 00:35:48 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.627 | 🔺 Rising |
| 2026-06-07 00:02:36 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 00:05:04 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 00:02:34 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-07 00:08:47 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:02:13 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:01:11 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:07:58 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:36:37 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:11:13 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:03:34 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:41 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-06 23:03:28 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:02:09 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:03:47 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:02:16 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:10:31 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:06:58 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:03:37 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:05:19 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:14:49 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 00:05:08 | Ellagawa (Kalu Ganga) | 7.14 | 🟢 Normal | -0.009 |  |
| 2026-06-07 00:05:28 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-06-07 00:04:24 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-07 00:06:42 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-07 00:02:55 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-06-07 00:06:18 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-06-07 00:01:18 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-06-07 00:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.011 |  |
| 2026-06-07 00:01:21 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.021 |  |
| 2026-06-07 00:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | -0.023 |  |
| 2026-06-07 00:03:00 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.023 |  |
| 2026-06-07 00:09:27 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | -0.028 |  |
| 2026-06-07 00:04:25 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-06-07 00:03:01 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.050 |  |
| 2026-06-07 00:04:23 | Rathnapura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)