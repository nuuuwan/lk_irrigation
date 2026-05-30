# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_21:14:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,036 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 21:14:17 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:12:46 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:10:55 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:08:31 | Ellagawa (Kalu Ganga) | 6.95 | 🟢 Normal | -0.065 |  |
| 2026-05-30 21:07:22 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | -0.019 |  |
| 2026-05-30 21:05:51 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | -0.029 |  |
| 2026-05-30 21:05:40 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:05:23 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-30 21:04:46 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-30 21:04:38 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 21:04:16 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.043 |  |
| 2026-05-30 21:04:12 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-05-30 21:04:12 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.022 |  |
| 2026-05-30 21:03:58 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.011 |  |
| 2026-05-30 21:03:57 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-30 21:03:44 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:03:26 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-05-30 21:03:16 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:03:12 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-05-30 21:03:09 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:03:09 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.051 |  |
| 2026-05-30 21:03:05 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:03:03 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:02:57 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:02:39 | Hanwella (Kelani Ganga) | 2.49 | 🟢 Normal | -0.050 |  |
| 2026-05-30 21:02:37 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-30 21:02:25 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.036 |  |
| 2026-05-30 21:02:07 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:02:06 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | -0.057 |  |
| 2026-05-30 21:01:55 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.011 |  |
| 2026-05-30 21:01:44 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:01:26 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:01:12 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-30 21:01:00 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.016 |  |
| 2026-05-30 20:35:25 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 21:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | -0.057 |  |
| 2026-05-30 21:03:57 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-30 21:04:46 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-30 21:01:12 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-30 21:04:38 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 18:00:56 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:02:06 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:03:09 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:12:46 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:03:44 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:01:44 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:01:26 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:03:03 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:05:40 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:02:57 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:02:07 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:31 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:03:16 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:14:17 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:03:05 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:04:12 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-05-30 21:03:26 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-05-30 21:02:37 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-30 21:05:23 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-30 21:03:12 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-05-30 21:01:55 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.011 |  |
| 2026-05-30 21:03:58 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.011 |  |
| 2026-05-30 21:01:00 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.016 |  |
| 2026-05-30 21:07:22 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | -0.019 |  |
| 2026-05-30 21:04:12 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.022 |  |
| 2026-05-30 21:05:51 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | -0.029 |  |
| 2026-05-30 21:02:25 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.036 |  |
| 2026-05-30 21:04:16 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.043 |  |
| 2026-05-30 21:02:39 | Hanwella (Kelani Ganga) | 2.49 | 🟢 Normal | -0.050 |  |
| 2026-05-30 21:03:09 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.051 |  |
| 2026-05-30 21:08:31 | Ellagawa (Kalu Ganga) | 6.95 | 🟢 Normal | -0.065 |  |
| 2026-05-30 18:02:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -30.857 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)