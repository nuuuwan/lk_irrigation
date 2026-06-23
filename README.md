# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_09:13:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,044 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 09:13:08 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:11:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | 0.038 | 🔺 Rising |
| 2026-06-23 09:11:36 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -0.019 |  |
| 2026-06-23 09:11:06 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-06-23 09:09:59 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.028 |  |
| 2026-06-23 09:09:47 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.115 |  |
| 2026-06-23 09:09:24 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:07:49 | Rathnapura (Kalu Ganga) | 3.56 | 🟢 Normal | -0.109 |  |
| 2026-06-23 09:07:30 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.039 |  |
| 2026-06-23 09:07:25 | Glencourse (Kelani Ganga) | 12.68 | 🟢 Normal | -0.177 |  |
| 2026-06-23 09:06:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:06:26 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-23 09:06:19 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.137 |  |
| 2026-06-23 09:05:32 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-23 09:05:18 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:05:02 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-23 09:04:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.203 |  |
| 2026-06-23 09:04:21 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | -0.020 |  |
| 2026-06-23 09:04:12 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:04:01 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:03:40 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-23 09:03:31 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:03:13 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | -0.049 |  |
| 2026-06-23 09:03:06 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:03:01 | Badalgama (Maha Oya) | 3.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 09:02:30 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 09:02:09 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:01:58 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-06-23 09:01:50 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:01:45 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-06-23 09:01:45 | Magura (Kalu Ganga) | 3.72 | 🟢 Normal | -0.133 |  |
| 2026-06-23 09:01:43 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.040 |  |
| 2026-06-23 09:01:42 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | 0.022 | 🔺 Rising |
| 2026-06-23 09:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-06-23 09:01:15 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:01:01 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-23 09:00:21 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-23 08:24:11 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.058 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 09:11:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | 0.038 | 🔺 Rising |
| 2026-06-23 09:01:42 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | 0.022 | 🔺 Rising |
| 2026-06-23 09:11:06 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-06-23 09:05:02 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-23 09:06:26 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-23 09:03:40 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-23 09:03:01 | Badalgama (Maha Oya) | 3.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 09:02:30 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 08:16:29 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-23 09:01:50 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:03:31 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:06:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:09:24 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:13:08 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:04:12 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:05:18 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:04:01 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:01:15 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 08:18:06 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:03:06 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:02:09 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:05:32 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-23 09:01:01 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-23 09:11:36 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -0.019 |  |
| 2026-06-23 09:04:21 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | -0.020 |  |
| 2026-06-23 09:01:58 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-06-23 09:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-06-23 09:09:59 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.028 |  |
| 2026-06-23 09:07:30 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.039 |  |
| 2026-06-23 09:01:43 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.040 |  |
| 2026-06-23 09:01:45 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-06-23 09:03:13 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | -0.049 |  |
| 2026-06-23 08:24:11 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.058 |  |
| 2026-06-23 09:07:49 | Rathnapura (Kalu Ganga) | 3.56 | 🟢 Normal | -0.109 |  |
| 2026-06-23 09:09:47 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.115 |  |
| 2026-06-23 09:01:45 | Magura (Kalu Ganga) | 3.72 | 🟢 Normal | -0.133 |  |
| 2026-06-23 09:06:19 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.137 |  |
| 2026-06-23 09:07:25 | Glencourse (Kelani Ganga) | 12.68 | 🟢 Normal | -0.177 |  |
| 2026-06-23 09:04:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.203 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)