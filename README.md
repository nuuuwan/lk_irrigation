# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_13:27:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,680 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 13:27:09 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:17:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:16:56 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-28 13:16:35 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:12:12 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:12:10 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 36.344 | 🔺 Rising |
| 2026-06-28 13:11:47 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:11:41 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.027 |  |
| 2026-06-28 13:10:29 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:09:55 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:08:41 | Panadugama (Nilwala Ganga) | 0.33 | 🟢 Normal | 36.344 | 🔺 Rising |
| 2026-06-28 13:08:21 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.072 |  |
| 2026-06-28 13:07:46 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.058 |  |
| 2026-06-28 13:07:40 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:06:55 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:06:24 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:05:20 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-06-28 13:05:16 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-28 13:05:11 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.068 |  |
| 2026-06-28 13:04:12 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:04:00 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-06-28 13:03:53 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:03:42 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-06-28 13:03:01 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-28 13:02:55 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:02:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:02:02 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:02:02 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:02:01 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-06-28 13:02:01 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | -0.011 |  |
| 2026-06-28 13:01:54 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:01:45 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:01:44 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:01:15 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-28 13:01:00 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:00:47 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:00:43 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-06-28 13:00:22 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-06-28 13:00:15 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-28 12:58:45 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 13:12:10 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 36.344 | 🔺 Rising |
| 2026-06-28 13:01:15 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-28 13:05:16 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-28 13:00:15 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-28 11:15:41 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-28 13:16:56 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-28 13:01:44 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:01:54 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:02:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:00:47 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:03:53 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:16:35 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:06:55 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:04:12 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:12:12 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:01:00 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:01:45 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:11:47 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:02:55 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:06:24 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:27:09 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:10:29 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:07:40 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:02:02 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:17:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:05:20 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-06-28 13:03:01 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-28 13:04:00 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-06-28 13:02:01 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-06-28 13:00:43 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-06-28 13:02:01 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | -0.011 |  |
| 2026-06-28 13:03:42 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-06-28 13:00:22 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-06-28 13:11:41 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.027 |  |
| 2026-06-28 13:07:46 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.058 |  |
| 2026-06-28 13:05:11 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.068 |  |
| 2026-06-28 13:08:21 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.072 |  |
| 2026-06-28 12:08:48 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)