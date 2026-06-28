# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_07:43:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,443 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 07:43:40 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.006 |  |
| 2026-06-28 07:27:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.53 | 🟢 Normal | -0.119 |  |
| 2026-06-28 07:17:58 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.008 |  |
| 2026-06-28 07:15:33 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:14:25 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.027 |  |
| 2026-06-28 07:13:47 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.033 |  |
| 2026-06-28 07:09:53 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.027 |  |
| 2026-06-28 07:08:42 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-06-28 07:08:04 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.046 |  |
| 2026-06-28 07:07:23 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:06:40 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:06:27 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:06:11 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.010 |  |
| 2026-06-28 07:06:05 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-28 07:04:43 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.108 |  |
| 2026-06-28 07:04:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:04:27 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.144 |  |
| 2026-06-28 07:03:46 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-28 07:03:31 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-06-28 07:03:19 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:03:06 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:02:55 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-28 07:02:54 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:02:43 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 07:02:25 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-28 07:02:19 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:02:14 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:02:09 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | -0.005 |  |
| 2026-06-28 07:02:06 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.063 |  |
| 2026-06-28 07:01:57 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:01:55 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 07:01:47 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-06-28 07:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:01:39 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:00:36 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.062 |  |
| 2026-06-28 07:00:15 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:00:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 07:06:05 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-28 07:02:55 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-28 07:02:43 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 07:01:55 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 07:02:19 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:01:39 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:04:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:15:33 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:07:23 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:06:27 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:03:19 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:03:06 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:02:54 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:02:14 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:06:40 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-28 06:00:45 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:01:57 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:00:15 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-28 07:02:09 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | -0.005 |  |
| 2026-06-28 07:43:40 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.006 |  |
| 2026-06-28 07:17:58 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.008 |  |
| 2026-06-28 07:03:46 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-28 07:06:11 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.010 |  |
| 2026-06-28 07:02:25 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-28 07:00:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-06-28 07:03:31 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-06-28 07:01:47 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-06-28 06:01:14 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.017 |  |
| 2026-06-28 07:08:42 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-06-28 07:14:25 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.027 |  |
| 2026-06-28 07:09:53 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.027 |  |
| 2026-06-28 07:13:47 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.033 |  |
| 2026-06-28 07:08:04 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.046 |  |
| 2026-06-28 07:00:36 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.062 |  |
| 2026-06-28 07:02:06 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.063 |  |
| 2026-06-28 07:04:43 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.108 |  |
| 2026-06-28 07:27:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.53 | 🟢 Normal | -0.119 |  |
| 2026-06-28 07:04:27 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)