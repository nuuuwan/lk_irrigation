# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_13:18:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **180,067 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 13:18:24 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:11:28 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:09:47 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.018 |  |
| 2026-06-15 13:09:21 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-06-15 13:08:16 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-06-15 13:08:05 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:07:33 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 13:08:16 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-06-15 13:03:05 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-15 13:03:28 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-15 13:04:17 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:01:14 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:00:41 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:01:56 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:08:05 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:07:33 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:01:35 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:18:24 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:02:47 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:03:14 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:00:15 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:01:21 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:02:57 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:11:28 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:03:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:02:08 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-15 13:09:21 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-06-15 13:05:14 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-06-15 13:03:35 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-06-15 13:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-15 13:02:41 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-06-15 13:01:34 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-06-15 13:04:02 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.011 |  |
| 2026-06-15 13:00:39 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-06-15 13:09:47 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.018 |  |
| 2026-06-15 13:00:44 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.020 |  |
| 2026-06-15 13:03:21 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.023 |  |
| 2026-06-15 13:03:14 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | -0.030 |  |
| 2026-06-15 13:04:20 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.031 |  |
| 2026-06-15 13:05:56 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.045 |  |
| 2026-06-15 13:04:03 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.069 |  |
| 2026-06-15 13:02:10 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.071 |  |
| 2026-06-15 13:06:03 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | -0.076 |  |
| 2026-06-15 13:02:48 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.079 |  |
| 2026-06-15 13:05:59 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.091 |  |
| 2026-06-15 13:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.81 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)