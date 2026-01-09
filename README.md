# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_00:14:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,326 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 00:14:05 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -36.000 |  |
| 2026-01-10 00:14:03 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -36.000 |  |
| 2026-01-10 00:11:08 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-10 00:10:01 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:08:54 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.018 |  |
| 2026-01-10 00:08:48 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:08:45 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.106 |  |
| 2026-01-10 00:07:17 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:07:14 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-10 00:06:53 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.046 |  |
| 2026-01-10 00:06:10 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:06:02 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:05:53 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-10 00:05:37 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-10 00:05:36 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-10 00:05:23 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-10 00:04:59 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-01-10 00:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-10 00:04:23 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:04:16 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:04:06 | Padiyathalawa (Maduru Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 00:03:31 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:03:29 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:03:24 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.060 |  |
| 2026-01-10 00:03:07 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:02:59 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:02:54 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:02:41 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:02:25 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:02:25 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:02:13 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-10 00:01:50 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:01:26 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-10 00:01:26 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-01-10 00:01:18 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:36:08 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 00:05:23 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-10 00:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-10 00:05:36 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-10 00:11:08 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-10 00:01:26 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-09 17:13:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 00:07:14 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-10 00:04:06 | Padiyathalawa (Maduru Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 00:02:25 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:01:18 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:02:41 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:02:54 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:07:17 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:03:07 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:03:31 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:10:01 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:02:59 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:03:29 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:01:50 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:06:02 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:06:10 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:04:23 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 23:04:09 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:04:16 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:02:25 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:08:48 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:02:13 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-10 00:05:53 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-10 00:05:37 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:08:00 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-10 00:08:54 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.018 |  |
| 2026-01-10 00:01:26 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-01-10 00:04:59 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-01-10 00:06:53 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.046 |  |
| 2026-01-10 00:03:24 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.060 |  |
| 2026-01-10 00:08:45 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.106 |  |
| 2026-01-10 00:14:05 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)