# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_08:08:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,865 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 08:08:29 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:08:25 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:08:24 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-15 08:07:17 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-06-15 08:06:52 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.012 |  |
| 2026-06-15 08:06:29 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:06:07 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-15 08:05:54 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.210 |  |
| 2026-06-15 08:05:05 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:05:00 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | -0.069 |  |
| 2026-06-15 08:04:52 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:04:09 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.020 |  |
| 2026-06-15 08:04:06 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.020 |  |
| 2026-06-15 08:04:01 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.039 |  |
| 2026-06-15 08:03:42 | Ellagawa (Kalu Ganga) | 6.62 | 🟢 Normal | -0.109 |  |
| 2026-06-15 08:03:40 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.021 |  |
| 2026-06-15 08:03:36 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-06-15 08:03:33 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:03:29 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-06-15 08:03:24 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.024 |  |
| 2026-06-15 08:03:23 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-06-15 08:02:51 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.032 |  |
| 2026-06-15 08:02:43 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-06-15 08:02:34 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:02:33 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-15 08:02:24 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-15 08:02:19 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.022 |  |
| 2026-06-15 08:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | -0.080 |  |
| 2026-06-15 08:02:04 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:01:44 | Putupaula (Kalu Ganga) | 2.11 | 🟢 Normal | -0.046 |  |
| 2026-06-15 08:00:40 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-06-15 08:00:30 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:00:30 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.045 |  |
| 2026-06-15 08:00:17 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.061 |  |
| 2026-06-15 08:00:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:59:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:45:53 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.210 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 08:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | -0.080 |  |
| 2026-06-15 08:02:24 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-15 08:03:29 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-06-15 08:06:07 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-15 08:02:34 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:00:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:04:52 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:08:29 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:59:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:06:29 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:08:25 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:03:33 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:04:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:05:05 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:05:17 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:00:30 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:02:04 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-15 08:07:17 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-06-15 08:02:33 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-15 08:08:24 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-15 08:03:23 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-06-15 08:00:40 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-06-15 07:01:26 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-06-15 08:06:52 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.012 |  |
| 2026-06-15 08:03:36 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-06-15 08:04:09 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.020 |  |
| 2026-06-15 08:02:43 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-06-15 08:04:06 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.020 |  |
| 2026-06-15 08:03:40 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.021 |  |
| 2026-06-15 08:02:19 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.022 |  |
| 2026-06-15 08:03:24 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.024 |  |
| 2026-06-15 08:02:51 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.032 |  |
| 2026-06-15 08:04:01 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.039 |  |
| 2026-06-15 08:00:30 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.045 |  |
| 2026-06-15 08:01:44 | Putupaula (Kalu Ganga) | 2.11 | 🟢 Normal | -0.046 |  |
| 2026-06-15 08:00:17 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.061 |  |
| 2026-06-15 08:05:00 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | -0.069 |  |
| 2026-06-15 08:03:42 | Ellagawa (Kalu Ganga) | 6.62 | 🟢 Normal | -0.109 |  |
| 2026-06-15 08:05:54 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)