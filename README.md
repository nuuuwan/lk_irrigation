# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_07:04:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,131 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 07:04:17 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-06-12 07:04:00 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-12 07:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.029 |  |
| 2026-06-12 07:03:34 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-06-12 07:03:27 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 07:03:15 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 07:03:14 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.013 |  |
| 2026-06-12 07:03:03 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | -0.134 |  |
| 2026-06-12 07:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.247 | 🔺 Rising |
| 2026-06-12 07:02:30 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-12 07:02:29 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 07:02:28 | Deraniyagala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.109 |  |
| 2026-06-12 07:02:11 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-12 07:02:08 | Putupaula (Kalu Ganga) | 1.66 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-06-12 07:01:49 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-12 07:01:41 | Ellagawa (Kalu Ganga) | 7.88 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-06-12 07:01:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-12 07:01:13 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 07:00:48 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.002 |  |
| 2026-06-12 07:00:30 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-12 06:30:36 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 06:16:44 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 07:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.247 | 🔺 Rising |
| 2026-06-12 06:02:31 | Magura (Kalu Ganga) | 4.28 | 🟡 Alert | 0.210 | 🔺 Rising |
| 2026-06-12 06:06:52 | Rathnapura (Kalu Ganga) | 5.95 | 🟡 Alert | 0.095 | 🔺 Rising |
| 2026-06-12 06:02:41 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | 1.674 | 🔺 Rising |
| 2026-06-12 06:09:38 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.416 | 🔺 Rising |
| 2026-06-12 07:04:17 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-06-12 06:02:15 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-06-12 06:06:31 | Holombuwa (Kelani Ganga) | 1.99 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-06-12 07:01:41 | Ellagawa (Kalu Ganga) | 7.88 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-06-12 07:03:34 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-06-12 07:02:08 | Putupaula (Kalu Ganga) | 1.66 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-06-12 06:08:01 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-06-12 07:02:30 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-12 06:08:43 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-12 06:02:49 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-12 07:01:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-12 07:04:00 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-12 06:00:41 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 07:03:15 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 06:06:33 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 06:05:45 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-12 07:02:11 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-12 07:01:13 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 07:02:29 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 06:30:36 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:11:49 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-12 07:03:27 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 07:01:49 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-12 06:01:32 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-12 06:04:58 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-12 07:00:30 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-12 07:00:48 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.002 |  |
| 2026-06-12 07:03:14 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.013 |  |
| 2026-06-12 06:04:44 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.019 |  |
| 2026-06-12 06:03:38 | Glencourse (Kelani Ganga) | 12.03 | 🟢 Normal | -0.023 |  |
| 2026-06-12 07:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.029 |  |
| 2026-06-12 06:02:53 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | -0.107 |  |
| 2026-06-12 07:02:28 | Deraniyagala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.109 |  |
| 2026-06-12 07:03:03 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)