# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_07:28:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,244 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 07:28:15 | Rathnapura (Kalu Ganga) | 4.21 | 🟢 Normal | -0.111 |  |
| 2026-06-30 07:12:35 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.091 |  |
| 2026-06-30 07:12:27 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.053 |  |
| 2026-06-30 07:09:46 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.058 |  |
| 2026-06-30 07:08:59 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:08:49 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:07:25 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.109 |  |
| 2026-06-30 07:07:05 | Baddegama (Gin Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:07:03 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:06:44 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.147 |  |
| 2026-06-30 07:05:53 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:04:33 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:04:20 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.064 |  |
| 2026-06-30 07:04:10 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.028 |  |
| 2026-06-30 07:04:08 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:04:04 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.091 |  |
| 2026-06-30 07:04:01 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-06-30 07:03:52 | Hanwella (Kelani Ganga) | 3.31 | 🟢 Normal | -0.141 |  |
| 2026-06-30 07:03:30 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:03:08 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.031 |  |
| 2026-06-30 07:03:06 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:02:54 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 07:02:51 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:02:49 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:02:33 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 07:02:31 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.73 | 🟢 Normal | -0.132 |  |
| 2026-06-30 07:02:21 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-30 07:01:39 | Ellagawa (Kalu Ganga) | 7.97 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-06-30 07:01:26 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:01:24 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:01:17 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-06-30 07:01:17 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.002 |  |
| 2026-06-30 07:01:00 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-30 07:00:46 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.013 |  |
| 2026-06-30 07:00:38 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 07:02:21 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-30 07:01:00 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-30 07:02:54 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 07:02:33 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 07:01:17 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.002 |  |
| 2026-06-30 07:08:59 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:03:30 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:02:31 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:04:08 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:01:24 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:05:53 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:02:51 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:03:06 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:01:39 | Ellagawa (Kalu Ganga) | 7.97 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:07:05 | Baddegama (Gin Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:04:33 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:02:49 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:08:49 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:02:55 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:01:26 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:07:03 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-30 07:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-06-30 07:00:46 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.013 |  |
| 2026-06-30 07:04:01 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-06-30 07:01:17 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-06-30 07:04:10 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.028 |  |
| 2026-06-30 07:03:08 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.031 |  |
| 2026-06-30 07:00:38 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.042 |  |
| 2026-06-30 07:12:27 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.053 |  |
| 2026-06-30 07:09:46 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.058 |  |
| 2026-06-30 07:04:20 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.064 |  |
| 2026-06-30 07:12:35 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.091 |  |
| 2026-06-30 07:04:04 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.091 |  |
| 2026-06-30 07:07:25 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.109 |  |
| 2026-06-30 07:28:15 | Rathnapura (Kalu Ganga) | 4.21 | 🟢 Normal | -0.111 |  |
| 2026-06-30 07:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.73 | 🟢 Normal | -0.132 |  |
| 2026-06-30 07:03:52 | Hanwella (Kelani Ganga) | 3.31 | 🟢 Normal | -0.141 |  |
| 2026-06-30 07:06:44 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)