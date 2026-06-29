# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_16:01:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,660 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 16:01:16 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 16:01:13 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-29 16:00:56 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-06-29 16:00:56 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-06-29 16:00:37 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-29 16:00:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:18:22 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:12:25 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.018 |  |
| 2026-06-29 15:12:04 | Panadugama (Nilwala Ganga) | 4.44 | 🟢 Normal | 0.036 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 15:07:07 | Rathnapura (Kalu Ganga) | 6.19 | 🟡 Alert | 0.162 | 🔺 Rising |
| 2026-06-29 15:06:55 | Glencourse (Kelani Ganga) | 11.86 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-06-29 15:05:47 | Hanwella (Kelani Ganga) | 2.64 | 🟢 Normal | 0.331 | 🔺 Rising |
| 2026-06-29 15:03:10 | Deraniyagala (Kelani Ganga) | 2.28 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-06-29 15:01:28 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-06-29 15:03:07 | Ellagawa (Kalu Ganga) | 6.82 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-06-29 15:02:28 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-06-29 15:10:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.53 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-06-29 15:12:04 | Panadugama (Nilwala Ganga) | 4.44 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-29 15:00:26 | Magura (Kalu Ganga) | 3.25 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-29 15:08:26 | Baddegama (Gin Ganga) | 2.83 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-29 15:08:24 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-29 15:03:27 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-29 15:06:33 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 15:05:55 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 15:03:57 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:02:22 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:02:09 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-29 16:01:16 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:18:22 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:01:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 16:00:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:02:29 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:03:39 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:05:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:06:25 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:01:25 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 16:01:13 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:06:38 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:01:15 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:02:13 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 15:02:32 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-29 16:00:56 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-06-29 15:08:09 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-06-29 15:12:25 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.018 |  |
| 2026-06-29 16:00:56 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-06-29 15:01:23 | Nawalapitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.031 |  |
| 2026-06-29 15:04:22 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.063 |  |
| 2026-06-29 15:03:05 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)