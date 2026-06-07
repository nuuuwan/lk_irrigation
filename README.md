# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_06:33:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,643 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 06:33:29 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.001 |  |
| 2026-06-07 06:19:12 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:17:15 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:15:46 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-06-07 06:13:42 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | -0.009 |  |
| 2026-06-07 06:11:35 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:09:48 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:09:41 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-07 06:08:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 06:07:18 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.388 | 🔺 Rising |
| 2026-06-07 06:07:10 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 06:05:55 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.030 |  |
| 2026-06-07 06:05:55 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-06-07 06:05:42 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.019 |  |
| 2026-06-07 06:05:07 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:04:56 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:04:39 | Nawalapitiya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.673 | 🔺 Rising |
| 2026-06-07 06:04:37 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:03:53 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-06-07 06:03:49 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.049 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 06:02:42 | Deraniyagala (Kelani Ganga) | 2.58 | 🟢 Normal | 0.952 | 🔺 Rising |
| 2026-06-07 06:04:39 | Nawalapitiya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.673 | 🔺 Rising |
| 2026-06-07 06:01:46 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.422 | 🔺 Rising |
| 2026-06-07 06:07:18 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.388 | 🔺 Rising |
| 2026-06-07 06:00:37 | Rathnapura (Kalu Ganga) | 3.26 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-06-07 06:05:55 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-06-07 06:03:18 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-06-07 06:03:53 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-06-07 06:01:11 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-07 06:09:41 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-07 06:03:49 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-07 06:00:39 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-07 06:08:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 06:07:10 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 06:02:01 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-07 06:03:23 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 05:03:52 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:02:44 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:09:48 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:11:35 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:04:56 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:41 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:05:07 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:02:55 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:02:47 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:02:07 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:19:12 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:02:15 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:04:37 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 06:33:29 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.001 |  |
| 2026-06-07 06:03:11 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.005 |  |
| 2026-06-07 06:13:42 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | -0.009 |  |
| 2026-06-07 06:05:42 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.019 |  |
| 2026-06-07 06:15:46 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-06-07 06:03:17 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | -0.020 |  |
| 2026-06-07 06:01:12 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-06-07 06:05:55 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.030 |  |
| 2026-06-07 06:00:54 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)