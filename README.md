# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_08:43:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,971 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 08:43:30 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:13:09 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-26 08:12:21 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.017 |  |
| 2026-05-26 08:11:40 | Rathnapura (Kalu Ganga) | 4.98 | 🟢 Normal | -0.046 |  |
| 2026-05-26 08:10:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.17 | 🟡 Alert | 0.053 | 🔺 Rising |
| 2026-05-26 08:09:20 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-26 08:08:40 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:08:37 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:07:45 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.205 |  |
| 2026-05-26 08:06:31 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-05-26 08:06:16 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:05:45 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:05:45 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | -0.032 |  |
| 2026-05-26 08:05:01 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:04:50 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:03:47 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-26 08:03:29 | Deraniyagala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.149 |  |
| 2026-05-26 08:03:25 | Glencourse (Kelani Ganga) | 12.28 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-05-26 08:03:14 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-26 08:03:11 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 08:03:09 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:03:02 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2026-05-26 08:02:59 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-26 08:02:31 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:02:31 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:02:27 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 08:02:17 | Dunamale (Aththanagalu Oya) | 2.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 08:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.082 |  |
| 2026-05-26 08:02:03 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.075 |  |
| 2026-05-26 08:02:01 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.096 |  |
| 2026-05-26 08:01:35 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:01:33 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.042 |  |
| 2026-05-26 08:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:01:25 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:01:11 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.005 |  |
| 2026-05-26 08:00:41 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:00:12 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.073 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 08:10:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.17 | 🟡 Alert | 0.053 | 🔺 Rising |
| 2026-05-26 08:03:25 | Glencourse (Kelani Ganga) | 12.28 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-05-26 08:03:14 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-26 08:03:47 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-26 08:02:59 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-26 08:13:09 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-26 08:09:20 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-26 08:02:17 | Dunamale (Aththanagalu Oya) | 2.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 08:03:11 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 08:02:27 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 08:01:25 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:00:41 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:08:40 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:01:35 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:05:01 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:43:30 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:03:09 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:05:45 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:02:31 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:02:23 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:08:37 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:06:16 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:02:31 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:04:50 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 08:01:11 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.005 |  |
| 2026-05-26 07:05:07 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-05-26 08:12:21 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.017 |  |
| 2026-05-26 08:06:31 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-05-26 08:05:45 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | -0.032 |  |
| 2026-05-26 08:01:33 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.042 |  |
| 2026-05-26 08:11:40 | Rathnapura (Kalu Ganga) | 4.98 | 🟢 Normal | -0.046 |  |
| 2026-05-26 08:03:02 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2026-05-26 08:00:12 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.073 |  |
| 2026-05-26 08:02:03 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.075 |  |
| 2026-05-26 08:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.082 |  |
| 2026-05-26 08:02:01 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.096 |  |
| 2026-05-26 08:03:29 | Deraniyagala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.149 |  |
| 2026-05-26 08:07:45 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)