# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_23:17:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **218,013 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-27 23:17:26 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:14:42 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:14:09 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.029 |  |
| 2026-07-27 23:14:05 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-07-27 23:10:31 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:07:50 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:06:49 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:06:13 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-07-27 23:06:08 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:06:05 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-07-27 23:05:45 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-07-27 23:05:41 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-07-27 23:05:40 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:04:51 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:04:48 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 23:04:41 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-07-27 23:03:16 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:03:12 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-07-27 23:02:58 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:02:45 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-27 23:02:44 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-07-27 23:02:36 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-07-27 23:02:32 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:02:03 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:01:58 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:01:43 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:01:33 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:01:22 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:01:14 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:01:04 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:00:20 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-27 23:05:45 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-07-27 23:02:45 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-27 23:04:48 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 22:06:58 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-27 23:01:43 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:00:20 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:01:04 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:01:14 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-27 22:03:28 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:01:33 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:10:31 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-27 22:01:39 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:03:06 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:07:50 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-27 22:02:38 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-27 22:09:27 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:02:32 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:01:22 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:01:58 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:06:49 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:17:26 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:03:16 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:06:08 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:02:03 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:00:30 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:04:51 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:05:40 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-27 21:16:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-27 23:14:05 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-07-27 23:06:13 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-07-27 23:05:41 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-07-27 23:06:05 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-07-27 23:02:36 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-07-27 23:03:12 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-07-27 23:04:41 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-07-27 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-07-27 23:02:44 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-07-27 23:14:09 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.029 |  |
| 2026-07-27 22:08:29 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)