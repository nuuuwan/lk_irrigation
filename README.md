# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_22:07:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,839 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 22:07:14 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-20 22:06:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.085 |  |
| 2026-06-20 22:06:06 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:06:05 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:04:57 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:04:17 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:04:16 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-20 22:03:42 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:03:37 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.031 |  |
| 2026-06-20 22:03:30 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-06-20 22:03:22 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-06-20 22:03:18 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:03:00 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.043 |  |
| 2026-06-20 22:02:53 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-06-20 22:02:29 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:02:27 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:02:27 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.021 |  |
| 2026-06-20 22:02:21 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:01:52 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:01:32 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 22:01:22 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:01:12 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-06-20 22:00:57 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-06-20 22:00:34 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:00:13 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:44:48 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:44:05 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 21:03:41 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.374 | 🔺 Rising |
| 2026-06-20 22:07:14 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-20 18:12:10 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-20 22:00:13 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:02:29 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:04:17 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:01:22 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:00:34 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:04:57 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:03:42 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:02:21 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:01:32 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:04:56 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:04:15 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:06:06 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:02:27 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:06:05 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:08:18 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:01:52 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:03:18 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:03:30 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-06-20 21:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-06-20 22:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:02:49 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-20 22:04:16 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-20 21:06:08 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-06-20 21:06:27 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.011 |  |
| 2026-06-20 22:00:57 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-06-20 22:02:53 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-06-20 22:02:27 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.021 |  |
| 2026-06-20 22:01:12 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-06-20 22:03:22 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-06-20 21:04:37 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.023 |  |
| 2026-06-20 22:03:37 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.031 |  |
| 2026-06-20 21:01:14 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.035 |  |
| 2026-06-20 22:03:00 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.043 |  |
| 2026-06-20 22:06:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.085 |  |
| 2026-06-20 21:05:33 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.239 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)