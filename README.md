# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_16:36:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **204,363 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 16:36:42 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:22:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-12 16:17:14 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:08:53 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:07:31 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:07:21 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-12 16:07:14 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:07:03 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:06:48 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:06:48 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-12 16:06:28 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:05:35 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:05:13 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:05:03 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-12 16:04:25 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:04:23 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-07-12 16:04:22 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.009 |  |
| 2026-07-12 16:04:14 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:03:59 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-07-12 16:03:32 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:03:16 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:03:03 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:02:59 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-07-12 16:02:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.096 |  |
| 2026-07-12 16:02:46 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:02:45 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:02:31 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.059 |  |
| 2026-07-12 16:02:19 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:01:44 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-12 16:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:01:10 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:01:08 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:01:05 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:01:04 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:01:03 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:00:50 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:00:35 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 16:02:59 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-07-12 16:06:48 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-12 16:01:44 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-12 16:22:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-12 16:05:03 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-12 16:07:21 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-12 16:01:03 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:01:10 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:00:35 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:07:48 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:36:42 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:00:50 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 15:05:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:17:14 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:01:08 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:05:35 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:03:16 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:07:03 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:03:03 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:07:14 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:02:45 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:06:48 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:01:04 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:05:13 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:06:28 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:04:25 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 16:04:22 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.009 |  |
| 2026-07-12 16:03:32 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:08:53 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:02:19 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:04:14 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:07:31 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:02:46 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:01:05 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-12 16:03:59 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-07-12 16:04:23 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-07-12 16:02:31 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.059 |  |
| 2026-07-12 16:02:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)