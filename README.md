# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_05:20:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,888 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 05:20:50 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-23 05:17:33 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:15:53 | Magura (Kalu Ganga) | 4.04 | 🟡 Alert | 0.036 | 🔺 Rising |
| 2026-06-23 05:11:41 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-23 05:11:11 | Rathnapura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.100 |  |
| 2026-06-23 05:08:58 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.252 |  |
| 2026-06-23 05:08:51 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.055 |  |
| 2026-06-23 05:07:12 | Giriulla (Maha Oya) | 2.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-23 05:07:02 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-06-23 05:06:34 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-06-23 05:06:26 | Deraniyagala (Kelani Ganga) | 2.46 | 🟢 Normal | 0.643 | 🔺 Rising |
| 2026-06-23 05:06:09 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:06:07 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:06:03 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -18.000 |  |
| 2026-06-23 05:06:01 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -18.000 |  |
| 2026-06-23 05:05:38 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.191 |  |
| 2026-06-23 05:05:28 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:04:50 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-23 05:04:38 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:04:34 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | 0.078 | 🔺 Rising |
| 2026-06-23 05:04:14 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:04:08 | Glencourse (Kelani Ganga) | 13.31 | 🟢 Normal | -0.069 |  |
| 2026-06-23 05:03:32 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.176 |  |
| 2026-06-23 05:02:35 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:02:27 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:02:27 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-06-23 05:02:21 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:02:16 | Hanwella (Kelani Ganga) | 4.93 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-23 05:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-06-23 05:02:10 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-23 05:02:08 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:01:51 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:01:47 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:01:41 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-23 05:01:21 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.022 |  |
| 2026-06-23 05:00:54 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-23 05:00:20 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 04:59:22 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.191 |  |
| 2026-06-23 04:35:17 | Rathnapura (Kalu Ganga) | 4.02 | 🟢 Normal | -0.100 |  |
| 2026-06-23 04:33:45 | Deraniyagala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.643 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 05:04:34 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | 0.078 | 🔺 Rising |
| 2026-06-23 04:00:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.77 | 🟡 Alert | 0.047 | 🔺 Rising |
| 2026-06-23 05:15:53 | Magura (Kalu Ganga) | 4.04 | 🟡 Alert | 0.036 | 🔺 Rising |
| 2026-06-23 05:06:26 | Deraniyagala (Kelani Ganga) | 2.46 | 🟢 Normal | 0.643 | 🔺 Rising |
| 2026-06-23 05:07:02 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-06-23 04:05:33 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-23 05:02:16 | Hanwella (Kelani Ganga) | 4.93 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-23 05:04:50 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-23 05:20:50 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-23 05:02:10 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-23 05:00:54 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-23 05:01:41 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-23 05:07:12 | Giriulla (Maha Oya) | 2.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-23 05:11:41 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-23 05:02:27 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:04:38 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:02:08 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:05:28 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:23 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:06:09 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:00:20 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:01:47 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:02:35 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:55 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:17:33 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-06-23 04:01:20 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:02:21 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-23 05:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-06-23 05:06:34 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-06-23 05:02:27 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-06-23 05:01:21 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.022 |  |
| 2026-06-22 18:01:33 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.029 |  |
| 2026-06-23 05:08:51 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.055 |  |
| 2026-06-23 05:04:08 | Glencourse (Kelani Ganga) | 13.31 | 🟢 Normal | -0.069 |  |
| 2026-06-23 05:11:11 | Rathnapura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.100 |  |
| 2026-06-23 05:03:32 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.176 |  |
| 2026-06-23 05:05:38 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.191 |  |
| 2026-06-23 05:08:58 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.252 |  |
| 2026-06-23 05:06:03 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)