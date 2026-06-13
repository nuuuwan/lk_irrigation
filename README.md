# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_16:17:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,392 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 16:17:44 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.016 |  |
| 2026-06-13 16:14:15 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.043 |  |
| 2026-06-13 16:11:28 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | 0.000 |  |
| 2026-06-13 16:09:00 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-06-13 16:08:11 | Panadugama (Nilwala Ganga) | 4.41 | 🟢 Normal | -0.032 |  |
| 2026-06-13 16:07:52 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:07:09 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:06:45 | Badalgama (Maha Oya) | 3.46 | 🟢 Normal | -0.010 |  |
| 2026-06-13 16:06:32 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-13 16:06:23 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.028 |  |
| 2026-06-13 16:06:11 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | 0.000 |  |
| 2026-06-13 16:06:07 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:05:37 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-13 16:05:31 | Rathnapura (Kalu Ganga) | 5.14 | 🟢 Normal | -0.067 |  |
| 2026-06-13 16:05:20 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:05:15 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 16:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.51 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-06-13 16:11:28 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | 0.000 |  |
| 2026-06-13 16:06:11 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | 0.000 |  |
| 2026-06-13 16:01:39 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-13 16:02:22 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-13 16:03:29 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-13 16:06:32 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-13 16:04:00 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-13 16:05:37 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-13 16:03:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-13 15:02:52 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:07:09 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:07:52 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:06:07 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:05:20 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:02:38 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:04:53 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:02:44 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:05:15 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:01:01 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:01:19 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.005 |  |
| 2026-06-13 16:09:00 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-06-13 16:06:45 | Badalgama (Maha Oya) | 3.46 | 🟢 Normal | -0.010 |  |
| 2026-06-13 16:02:36 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-06-13 16:00:47 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-13 16:04:02 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-06-13 16:02:15 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-06-13 16:17:44 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.016 |  |
| 2026-06-13 16:04:44 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.019 |  |
| 2026-06-13 16:03:13 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-06-13 16:06:23 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.028 |  |
| 2026-06-13 16:01:39 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.030 |  |
| 2026-06-13 16:02:49 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.031 |  |
| 2026-06-13 16:08:11 | Panadugama (Nilwala Ganga) | 4.41 | 🟢 Normal | -0.032 |  |
| 2026-06-13 16:02:30 | Galgamuwa (Mee Oya) | 1.55 | 🟢 Normal | -0.034 |  |
| 2026-06-13 16:14:15 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.043 |  |
| 2026-06-13 16:02:37 | Glencourse (Kelani Ganga) | 11.77 | 🟢 Normal | -0.051 |  |
| 2026-06-13 16:05:31 | Rathnapura (Kalu Ganga) | 5.14 | 🟢 Normal | -0.067 |  |
| 2026-06-13 16:00:48 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)