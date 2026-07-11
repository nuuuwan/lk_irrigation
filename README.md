# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_08:06:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,152 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 08:06:00 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-11 08:05:43 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:05:23 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-07-11 08:04:57 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:04:54 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:04:47 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.082 |  |
| 2026-07-11 08:04:26 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:04:12 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-11 08:03:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.066 |  |
| 2026-07-11 08:03:36 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-11 08:03:30 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-07-11 08:03:24 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:03:21 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-07-11 08:03:18 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.062 |  |
| 2026-07-11 08:03:11 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:03:11 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-11 08:03:11 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.012 |  |
| 2026-07-11 08:03:02 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:02:53 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.031 |  |
| 2026-07-11 08:02:05 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:02:00 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:01:53 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:01:40 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-07-11 08:01:37 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |
| 2026-07-11 08:00:57 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-07-11 08:00:54 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-11 08:00:45 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.106 |  |
| 2026-07-11 08:00:42 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:00:37 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-11 07:38:04 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.106 |  |
| 2026-07-11 07:23:52 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 07:22:02 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-11 07:19:33 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-11 07:19:31 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-11 07:14:53 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 08:06:00 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-11 08:00:54 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-11 08:04:12 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-11 08:03:11 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-11 08:03:36 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-11 07:04:42 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-11 07:01:46 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-11 07:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 08:01:53 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:02:05 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:05:43 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:03:24 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:00:37 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:02:53 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:03:02 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:04:57 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 07:22:02 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:03:11 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:04:54 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-07-11 07:10:30 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:00:42 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 07:14:53 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 07:07:10 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:02:00 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:04:26 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 08:05:23 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-07-11 07:04:18 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-07-11 08:03:30 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-07-11 08:00:57 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-07-11 08:01:37 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |
| 2026-07-11 08:03:21 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-07-11 08:03:11 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.012 |  |
| 2026-07-11 08:01:40 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-07-11 08:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.031 |  |
| 2026-07-11 08:03:18 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.062 |  |
| 2026-07-11 08:03:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.066 |  |
| 2026-07-11 08:04:47 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.082 |  |
| 2026-07-11 08:00:45 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.106 |  |
| 2026-07-11 07:06:52 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)