# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_09:16:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **219,265 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 09:16:48 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:15:31 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:11:44 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-29 09:11:04 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:10:29 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-07-29 09:10:08 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-07-29 09:09:27 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-29 09:09:18 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-07-29 09:08:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-29 09:07:44 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | -0.010 |  |
| 2026-07-29 09:07:26 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:06:59 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-29 09:06:59 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:05:32 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:04:45 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-29 09:03:52 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-07-29 09:03:49 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:03:45 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:03:44 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:03:40 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.052 |  |
| 2026-07-29 09:03:31 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:03:26 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 09:03:20 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:03:07 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:59 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:55 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:48 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:34 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:32 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:13 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:06 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:02 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:01:59 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-29 09:01:34 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-07-29 09:01:31 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:01:25 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:01:23 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:01:18 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:00:32 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-07-29 08:39:23 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 08:33:00 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 09:03:52 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-07-29 09:09:18 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-07-29 09:01:59 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-29 09:09:27 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-29 09:10:08 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-07-29 09:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-29 09:11:44 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-29 09:03:26 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 09:08:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-29 09:06:59 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-29 09:03:45 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:06 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:03:07 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:03:31 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:16:48 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:01:18 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:07:26 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:04:45 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:01:25 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:03:49 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:02 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:15:31 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:11:04 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:03:44 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:48 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:01:31 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:55 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:13 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:06:59 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:03:20 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:59 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:32 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:01:23 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:02:34 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 09:10:29 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-07-29 09:07:44 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | -0.010 |  |
| 2026-07-29 09:01:34 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-07-29 09:00:32 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-07-29 09:03:40 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)