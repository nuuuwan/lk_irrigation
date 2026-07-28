# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_08:06:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **218,326 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 08:06:25 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-07-28 08:05:44 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-28 08:05:38 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-28 08:04:57 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:04:16 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-28 08:04:15 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | -0.071 |  |
| 2026-07-28 08:04:05 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-28 08:03:58 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.030 |  |
| 2026-07-28 08:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:03:14 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:03:14 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:03:02 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:02:59 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:02:59 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:02:55 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:02:43 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-07-28 08:02:40 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:02:30 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-28 08:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:02:10 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:02:02 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:01:53 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-07-28 08:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:01:03 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | -0.035 |  |
| 2026-07-28 08:00:56 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:00:50 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:00:23 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 07:56:40 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-28 07:43:51 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | -0.035 |  |
| 2026-07-28 07:42:17 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-28 07:26:24 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.008 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 08:01:53 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-07-28 08:04:05 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-28 08:04:16 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-28 08:05:38 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-28 07:17:19 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-28 07:05:53 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-28 08:05:44 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-28 07:26:24 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-28 08:02:40 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:00:23 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 07:03:35 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:02:55 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:03:14 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:02:02 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:02:59 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-07-28 07:42:17 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:04:57 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:00:56 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-28 07:03:23 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-28 07:01:44 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:03:14 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:02:10 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:00:50 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:03:02 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 07:13:57 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-28 08:02:59 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-28 07:07:26 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-07-28 08:02:43 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-07-28 08:02:30 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-28 08:06:25 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-07-28 07:09:16 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.029 |  |
| 2026-07-28 08:03:58 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.030 |  |
| 2026-07-28 08:01:03 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | -0.035 |  |
| 2026-07-28 08:04:15 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | -0.071 |  |
| 2026-07-28 07:03:25 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.104 |  |
| 2026-07-28 07:05:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)