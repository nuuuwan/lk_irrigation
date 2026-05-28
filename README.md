# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_17:14:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,106 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 17:14:16 | Urawa (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-05-28 17:11:15 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:11:00 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-05-28 17:10:14 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:09:06 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:08:25 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:07:25 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:07:11 | Magura (Kalu Ganga) | 4.94 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-05-28 17:06:13 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:06:06 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-28 17:06:03 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.029 |  |
| 2026-05-28 17:05:32 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | -0.040 |  |
| 2026-05-28 17:04:51 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-28 17:04:39 | Panadugama (Nilwala Ganga) | 3.48 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-05-28 17:04:25 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.019 |  |
| 2026-05-28 17:04:12 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 17:04:05 | Pitabeddara (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-28 17:03:58 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:03:41 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-05-28 17:03:35 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 17:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.27 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-28 17:03:31 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:03:28 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-05-28 17:03:07 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:02:59 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-05-28 17:02:45 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-05-28 17:02:38 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-28 17:02:35 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-05-28 17:02:33 | Deraniyagala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-05-28 17:02:29 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:02:23 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.011 |  |
| 2026-05-28 17:02:11 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:01:26 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.010 |  |
| 2026-05-28 17:01:26 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.078 |  |
| 2026-05-28 17:01:11 | Baddegama (Gin Ganga) | 2.93 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-28 17:01:08 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 17:07:11 | Magura (Kalu Ganga) | 4.94 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-05-28 17:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.27 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-28 17:11:00 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-05-28 17:04:05 | Pitabeddara (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-28 17:14:16 | Urawa (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-05-28 17:02:45 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-05-28 17:03:41 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-05-28 17:04:39 | Panadugama (Nilwala Ganga) | 3.48 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-05-28 17:02:33 | Deraniyagala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-05-28 17:01:11 | Baddegama (Gin Ganga) | 2.93 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-28 17:04:51 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-28 17:06:06 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-28 17:03:35 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 17:04:12 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 17:01:00 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:11:15 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:09:06 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:00:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:06:13 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:07:25 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:03:31 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:03:58 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:03:07 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:10:14 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:01:08 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:08:25 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:00:56 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:02:11 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:02:29 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-28 17:03:28 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-05-28 17:02:38 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-28 17:01:26 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.010 |  |
| 2026-05-28 17:02:23 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.011 |  |
| 2026-05-28 17:02:35 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-05-28 17:04:25 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.019 |  |
| 2026-05-28 17:02:59 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-05-28 17:06:03 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.029 |  |
| 2026-05-28 17:05:32 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | -0.040 |  |
| 2026-05-28 17:01:26 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)