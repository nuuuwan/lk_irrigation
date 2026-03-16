# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_19:46:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,170 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 19:46:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.017 |  |
| 2026-03-16 19:23:53 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:18:45 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-03-16 19:18:24 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:12:48 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:12:08 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:11:40 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.052 |  |
| 2026-03-16 19:11:29 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:09:32 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:08:41 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:07:26 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-16 19:06:51 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:06:33 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.029 |  |
| 2026-03-16 19:06:01 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-16 19:05:28 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:05:27 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 19:05:13 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:04:43 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-16 19:04:40 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-16 19:04:28 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:04:25 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:02:53 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:02:42 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-03-16 19:02:37 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:02:29 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-03-16 19:02:26 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:02:10 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:01:49 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:01:46 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:01:40 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-16 19:01:11 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:01:11 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:01:02 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:00:41 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:00:23 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.090 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 19:02:42 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-03-16 19:00:23 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-16 19:07:26 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-16 19:04:40 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-16 19:06:01 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-16 19:05:27 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 19:02:37 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:01:11 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:01:46 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:18:24 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:04:59 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:11:29 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:23:53 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:00:41 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:02:26 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:02:53 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:08:41 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:01:02 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:09:32 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:04:28 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:05:13 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:12:48 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:06:51 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:04:25 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:01:49 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:01:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:05:28 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:12:08 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:01:11 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:02:10 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 19:04:43 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-16 19:01:40 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-16 19:46:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.017 |  |
| 2026-03-16 19:02:29 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-03-16 19:06:33 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.029 |  |
| 2026-03-16 19:18:45 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-03-16 19:11:40 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.052 |  |
| 2026-03-16 18:00:13 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)