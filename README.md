# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_02:43:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,781 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 02:43:27 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-23 02:34:40 | Holombuwa (Kelani Ganga) | 2.06 | 🟢 Normal | -0.084 |  |
| 2026-06-23 02:29:10 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:16:50 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -24.000 |  |
| 2026-06-23 02:16:47 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -24.000 |  |
| 2026-06-23 02:13:54 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.029 |  |
| 2026-06-23 02:10:37 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-23 02:08:06 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -10.000 |  |
| 2026-06-23 02:07:48 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -10.000 |  |
| 2026-06-23 02:07:25 | Glencourse (Kelani Ganga) | 13.35 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-23 02:07:19 | Magura (Kalu Ganga) | 3.95 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-23 02:05:57 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-06-23 02:05:44 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:05:13 | Hanwella (Kelani Ganga) | 4.12 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-06-23 02:05:05 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:04:00 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-06-23 02:03:17 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-06-23 02:03:02 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-23 02:02:47 | Deraniyagala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.209 |  |
| 2026-06-23 02:02:13 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:02:09 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:02:08 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-23 02:02:02 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-06-23 02:01:58 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.227 |  |
| 2026-06-23 02:01:52 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:01:21 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:01:05 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 02:02:02 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-06-23 01:17:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.54 | 🟡 Alert | 0.017 | 🔺 Rising |
| 2026-06-23 02:05:57 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-06-23 02:05:13 | Hanwella (Kelani Ganga) | 4.12 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-06-23 02:03:17 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-06-23 02:07:25 | Glencourse (Kelani Ganga) | 13.35 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-23 02:02:08 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-23 00:02:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-23 01:25:21 | Putupaula (Kalu Ganga) | 2.06 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-23 02:43:27 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-23 02:03:02 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-23 02:07:19 | Magura (Kalu Ganga) | 3.95 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-23 02:10:37 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-23 01:04:12 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 00:06:10 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 02:05:05 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:01:05 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:01:52 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:01:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:02:09 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:23 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:03:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:29:10 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:04:24 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:05:44 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:55 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:02:59 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:00:24 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:01:23 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:02:13 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-23 02:04:00 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-06-23 01:46:21 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.012 |  |
| 2026-06-23 02:13:54 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.029 |  |
| 2026-06-22 18:01:33 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.029 |  |
| 2026-06-23 02:34:40 | Holombuwa (Kelani Ganga) | 2.06 | 🟢 Normal | -0.084 |  |
| 2026-06-23 02:02:47 | Deraniyagala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.209 |  |
| 2026-06-23 02:01:58 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.227 |  |
| 2026-06-23 02:08:06 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -10.000 |  |
| 2026-06-23 02:16:50 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -24.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)