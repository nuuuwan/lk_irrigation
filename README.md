# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--23_14:22:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,235 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 14:22:16 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:17:50 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-23 14:15:06 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-23 14:14:45 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:12:30 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:11:10 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:10:25 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.018 |  |
| 2026-03-23 14:08:41 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:07:37 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-03-23 14:07:12 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:06:51 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-03-23 14:06:17 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-23 14:05:48 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:05:39 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.096 |  |
| 2026-03-23 14:04:27 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:04:12 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:03:51 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:03:34 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-03-23 14:03:13 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:02:53 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-03-23 14:02:44 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:02:35 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:02:29 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.077 |  |
| 2026-03-23 14:02:23 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:02:09 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:02:04 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:02:01 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:01:49 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-03-23 14:01:37 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:01:35 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:01:11 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:01:04 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:01:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-23 14:00:41 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:00:29 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 14:01:49 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-03-23 14:01:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-23 14:17:50 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-23 14:15:06 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-23 14:06:17 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-23 14:02:04 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:00:29 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:04:12 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:12:30 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-23 13:01:50 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:03:51 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:11:10 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:00:41 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:22:16 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:01:37 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:08:41 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:05:48 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 11:07:31 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:02:09 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:03:13 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:02:35 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:01:35 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:14:45 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:02:23 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-23 14:07:37 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-03-23 14:07:12 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:01:04 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:02:44 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:01:11 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:02:01 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:04:27 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-03-23 14:10:25 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.018 |  |
| 2026-03-23 14:06:51 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-03-23 14:03:34 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-03-23 14:02:53 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-03-23 14:02:29 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.077 |  |
| 2026-03-23 14:05:39 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)