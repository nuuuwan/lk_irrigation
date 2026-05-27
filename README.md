# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_17:30:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,209 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 17:30:23 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:21:26 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:12:06 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:10:40 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-27 17:10:14 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-05-27 17:08:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.057 |  |
| 2026-05-27 17:08:27 | Rathnapura (Kalu Ganga) | 3.99 | 🟢 Normal | -0.028 |  |
| 2026-05-27 17:07:34 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-27 17:07:26 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:07:02 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-05-27 17:06:52 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 17:06:14 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-27 17:05:46 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-05-27 17:05:31 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-27 17:05:12 | Magura (Kalu Ganga) | 3.51 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-05-27 17:05:04 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-27 17:04:05 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-27 17:03:59 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | -0.010 |  |
| 2026-05-27 17:03:13 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.067 |  |
| 2026-05-27 17:03:08 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:03:03 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:02:55 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:02:52 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 17:02:48 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-27 17:02:48 | Deraniyagala (Kelani Ganga) | 2.40 | 🟢 Normal | 0.592 | 🔺 Rising |
| 2026-05-27 17:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.33 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-05-27 17:02:34 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-27 17:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 17:02:29 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-05-27 17:02:26 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:02:14 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:02:11 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-27 17:01:42 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:01:33 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:01:08 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-05-27 17:01:03 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:00:51 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:00:42 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:00:15 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 17:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.33 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-05-27 17:02:48 | Deraniyagala (Kelani Ganga) | 2.40 | 🟢 Normal | 0.592 | 🔺 Rising |
| 2026-05-27 17:05:12 | Magura (Kalu Ganga) | 3.51 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-05-27 17:10:14 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-05-27 17:04:05 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-27 17:07:34 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-27 17:05:04 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-27 17:02:48 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-27 17:02:11 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-27 17:10:40 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-27 17:06:14 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-27 17:05:31 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-27 17:02:52 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 17:00:15 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 17:06:52 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 17:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 17:01:33 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:01:42 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:00:42 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:00:51 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:02:26 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:01:03 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:03:03 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:30:23 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:03:08 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:02:55 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:07:26 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:12:06 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:21:26 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:02:14 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 17:05:46 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-05-27 17:07:02 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-05-27 17:02:34 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-27 17:03:59 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | -0.010 |  |
| 2026-05-27 17:02:29 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-05-27 17:01:08 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-05-27 17:08:27 | Rathnapura (Kalu Ganga) | 3.99 | 🟢 Normal | -0.028 |  |
| 2026-05-27 17:08:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.057 |  |
| 2026-05-27 17:03:13 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)